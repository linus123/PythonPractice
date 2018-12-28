$pythonExec = "C:\Users\pherrera\AppData\Local\Programs\Python\Python36-32\python.exe"
$resultFile = "output.txt"

if (Test-Path $resultFile) {
    Remove-Item $resultFile
}

Get-Content .\10149.txt | &$pythonExec .\yahtzee.py > $resultFile
