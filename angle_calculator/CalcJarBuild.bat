: CalcJarBuild.bat
: Builds a new JAR file for AngleCalc
:
@ECHO Building the jar...
D:
cd Main\class_files\BUILD_JAR
jar cmf MANIFEST.MF GratingCalc.jar Main.class AngleCalculator.class AngleCalculator$1.class AngleCalculator$PrintCalculations.class sourceCode

@ECHO Jar has been created...
@PAUSE