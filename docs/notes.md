## 13/08/2022
### Done
- Added the foundation for the execution
- Added an action interface system
### To do
- [ ] **IMPORTANT:** Bunch of issues regarding my `Ttype`, `Stype` and `Token`. Need to decide concretely when to switch from one to the next. Maybe during AST generation? I need a format which will have everything I need for evaluation:
    - [ ] Some way of encapsulating identifiers, with information about their name and datatype
    - [ ] Using the same class to represent all other parts of the program.
