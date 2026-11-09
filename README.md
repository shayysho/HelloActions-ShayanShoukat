# HelloActions-ShayanShoukat

## Explanation of the Workflow

1. **What is the purpose of the `on` section?**
   It specifies the events that automatically or manually trigger the workflow to run.

2. **What does `workflow_dispatch` do?**
   It allows the workflow to be manually triggered from the GitHub Actions web interface.

3. **What does `runs-on` specify?**
   It specifies the operating system environment (runner machine) on which the job will execute (e.g., `ubuntu-latest`).

4. **Why is `actions/checkout` needed?**
   It checks out (downloads) the repository's source code onto the runner machine so the steps can access and run the files.

5. **What does the language setup action do?**
   It installs and configures the specified programming language runtime environment on the runner machine.

6. **What is the difference between compiling and running the program?**
   Compiling translates source code into machine code or executable binaries (for compiled languages like Java or C++), while running executes the compiled binary or script directly.

7. **Where can you see the program output?**
   In the workflow execution logs under the specific step in the GitHub Actions tab.

8. **What is the difference between a workflow, a job, and a step?**
   - **Workflow:** The entire automated process defined in a single YAML file.
   - **Job:** A set of steps executed sequentially on the same runner machine.
   - **Step:** An individual task within a job (such as running a command or action).

---

## AI Usage Statement
AI (Gemini) was used solely to help explain the lab instructions step-by-step and guide setup without performing the work independently.