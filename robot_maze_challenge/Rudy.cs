using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MazeChallenge
{
	public class Rudy : Bot
	{
		public Rudy(Maze maze, (int, int) start) : base(maze, start) { }


		public void Start()
		{


			/*
			this.GetSensorLeft();
			this.GetSensorRight();
			this.GetSensorFront();
			this.GetSensorTop();
			this.TurnLeft();
			this.TurnRight();
			this.MoveForward();
			*/

			RightHandOnWall();


		}

		public void RightHandOnWall()
		{
			/*
			In the world of corn mazes, they say that you can always escape the maze
			if you touch your right hand to the wall next to you and only move forward
			if your hand is on the wall. I want to try to get Rudy through this maze
			following something like this. There are some instances where it won't work,
			but let's just see if Rudy can pay attention to his surroundings and learn
			to avoid those possible traps.

			Trap 1: The infinite loop
			Trap 2: The long cooridor that was falsly considered an infintite loop
			*/

			// I did realize later in looking at the bot code that this is already being done
			const int charge = 999999; // lets give Rudy a way to stop if he just can't solve the maze
			System.Text.StringBuilder action_memory = new StringBuilder(); // to remeber all previous actions

			// Step 1 as we enter the maze is run forward until we hit a wall
			while(this.GetSensorTop() && action_memory.Length < charge && !this.GetSensorFront())
			{
				this.MoveForward();
				action_memory.Append('f');
			}

			// Step 2 is have Rudy turn left and touch his right hand to the wall
			this.TurnLeft();
			action_memory.Append('l');

			// Step 3 is to try hugging the right as often as the maze complexity will allow
			while(this.GetSensorTop() && action_memory.Length < charge)
			{
				// Note that we will always check to see if we are outside and always keep an eye on battery power

				// If there is a wall on the right and none in front, move forward
				if(this.GetSensorRight() && !this.GetSensorFront())
				{
					this.MoveForward();
					action_memory.Append('f');
				}
				// If there is no wall to the right, turn right and move forward
				else if(!this.GetSensorRight())
				{
					this.TurnRight();
					this.MoveForward();
					action_memory.Append('r');
					action_memory.Append('f');
				}
				// If there is a wall in front, turn left
				else if(this.GetSensorFront())
				{
					this.TurnLeft();
					action_memory.Append('l');
				}

				// Now we have to make use of Rudy's memory
				const int memory_chunk_size = 50; // this is just a guess to keep from doing this a lot
				const int room_for_error = 2; // since we sometimes do two actions in a single loop
				if((action_memory.Length % memory_chunk_size) < room_for_error)
				{
					// let's check if we are stuck in an infinite internal loop
					if(DetectLoop(action_memory.ToString()))
					{
						// If we are stuck in a loop, it seems the best way to get out would
						// be to turn left, walk forward until we hit a new wall, and turn left again
						// this way we should be setup to start hugging the right again
						this.TurnLeft();
						action_memory.Append('l');
						while(this.GetSensorTop() && action_memory.Length < charge && !this.GetSensorFront())
						{
							this.MoveForward();
							action_memory.Append('f');
						}
						this.TurnLeft();
						action_memory.Append('l');
					}
				}

			}
		}

		private bool DetectLoop(string action_memory)
		{
			/*
			This is basically some really simple machine learning. We are keeping a history of
			all actions that Rudy takes. Since we know those actions, we can occasionally check
			for loops. Basically all we are doing is taking substrings of the action history off
			the end. For this experiment, it's possible Rudy will loop 4+ times before we catch
			it, but that shouldn't enough to run him dead so we are not worried. As long as he
			figures it out eventually.
			*/

			const int min_pattern_size = 12; // we assume this is the minimum number of steps a loop can be
			const int num_loops = 2;
            int max_pattern_size = action_memory.Length / num_loops;
            // if we don't have enough history to do at least 3 loops of the minimum pattern size
            // just assume we don't need to do this yet
            if(max_pattern_size < min_pattern_size)
            {
                return false;
            }
            // int pattern_count_to_trigger = 3; // we will try to only allow the robot to loop 3-4 times
            int action_end = action_memory.Length - 1;
            // int curr_pattern_size = min_pattern_size;
            for(int i = min_pattern_size; i < max_pattern_size; i++)
            {
				// Note that I did check for three loops at a time, but I decided that was overkill
                int start_index = action_end - (i * num_loops);
                string loop_string_one = action_memory.Substring(start_index, i);
                // string loop_string_two = action_memory.Substring(start_index + i, i);
                string loop_string_three = action_memory.Substring(action_end - i, i);
                if(loop_string_one == loop_string_three)
                {
					// before we return, lets make sure this isn't just a long corridor of forward movements
					// we do this by making sure there are at least 4 right turns in the loop
					// this could be better, but it does get the job done
					int num_right_turns = 0;
					foreach(char action in loop_string_three)
                    {
						if (action == 'r')
							num_right_turns++;
                    }
					if(num_right_turns >= 4)
						return true;
                }
            }

            return false;
		}

		
	}

	
}
