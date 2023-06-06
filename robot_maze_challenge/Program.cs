using System;
using System.Collections.Generic;
using System.Text;

namespace MazeChallenge
{
	class Program
	{
		static void Main(string[] args)
		{
			var name = "Level1";
			//var name = "Level2";
			//var name = "Level3";
			//var name = "Level4";
			//var name = "Level10";

			var maze = Maze.Load(name);
			var rudy = new Rudy(maze, maze.RandomDrop());
			rudy.EnableGraphicalMaze();
			//rudy.EnableLog();

			rudy.Start();


			Console.SetCursorPosition(0, maze.Grid.GetUpperBound(1));
			if (rudy.GetSensorTop())
				throw new Exception("Rudy is still stuck in the maze");

			Console.WriteLine($"Rudy succesffuly escaped from {name}.");
		}
	}
}
