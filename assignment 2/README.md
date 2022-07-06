These functoins are for owner only - 
getOwnerBalance and viewDues are view functions as they are only reading and ensuring that the state variables state variables cannot be modified after calling them.

These are general funtcions - 
MulDiv and getCompoundInterest do not read or modify any state variables and returns only using the parameters passed to it or using the local variables contained insde of it.

also - settleDues and reqLoan functions modify the state variables contained within them.
