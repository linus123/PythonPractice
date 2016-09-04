$pythonExec = "C:\Users\Paul\AppData\Local\Programs\Python\Python35\python.exe"
$resultFile = "output.txt"

if (Test-Path $resultFile) {
    Remove-Item $resultFile
}

Get-Content .\10033.txt | &$pythonExec .\Interpreter.py > $resultFile
