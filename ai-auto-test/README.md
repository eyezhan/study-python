AI Automation Test Suite
========================

1. Directory structure and comments

  ├─cases: test cases scripts saved path.
  │
  ├─configs: configuration of projects saved path.
  │
  └─execution: execute directory; logs and reports saved path.

2. Environment set up
  Run the setup script in Windows PowerShell(x86).
  > cd <ai-auto-test directory>
  > .\setup_env.bat

3. How to execute test cases.
  Open Git Bash/CMD/Windows PowerShell(x86).
  Example for Git Bash:
      $ ./execute.sh [-p TEST_PLAN]
  Example for CMD:
      > execute.sh [-p TEST_PLAN]
  Example for Windows PowerShell(x86):
      > .\execute.sh [-p TEST_PLAN]

  Result logs save in logs folder.
  Excel report save in reports folder.
