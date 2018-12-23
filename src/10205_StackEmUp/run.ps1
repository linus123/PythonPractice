$pythonExec = "C:\Users\linus\AppData\Local\Programs\Python\Python35\python.exe"
$resultFile = "output.txt"

if (Test-Path $resultFile) {
    Remove-Item $resultFile
}

Get-Content .\10205.txt | &$pythonExec .\stack_em_up.py > $resultFile
