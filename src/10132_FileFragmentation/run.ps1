$pythonExec = "C:\Users\linus\AppData\Local\Programs\Python\Python37-32\python.exe"
$resultFile = "output.txt"

if (Test-Path $resultFile) {
    Remove-Item $resultFile
}

Get-Content .\10132.txt | &$pythonExec .\file_fragmentation.py > $resultFile
