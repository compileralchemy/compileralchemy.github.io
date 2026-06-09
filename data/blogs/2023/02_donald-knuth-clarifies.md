title: Donald Knuth Clarifies
---
🎉 At 85 years of age, Donald Knuth was kind enough to reply to my email.\n\nIn April, while writing \"Merge Sort and Its Early History\" ( https://lnkd.in/ecjByBbt ) , I stumbled upon the MOVEIN instruction.\n\nI could not find it in assembly programming references.\n\nGoogle returned I think few passing mentions.\n\nEven, more weirdly, folks at asm on IRC were unaware and as confused as myself.\n\nThis was at a stage where assembly was being defined, forget about that, even the architecture of the computer, the Von Neumann architecture was not popular. Neumann was himself trying out ideas.\n\nSo, I asked Donald Knuth, the author of the paper what it meant, here is his answer.\n\nI guess Osmar Mansoor, you were right, it was an interesting piece!

> Dear Abdur-Rahmaan,
> 
> Please excuse the fact that I haven't had time to look at your email
> message from April until today.
> 
> In that program, MOVEIN is not an instruction; it is a symbolic name
> for the address where a dynamically changing instruction will be
> stored. (His computer was a LOT different from what we have now!)
> 
> Line 41 of the program says that we should reserve one "storage tank"
> (RST 1) to be called MOVEIN. Line 46 puts a PIK instruction into
> that storage tank. Eventually, control is transferred so that
> the machine executes that PIK instruction (which moves a block
> of words into a sequence of short tanks called BUFFER).
> 
> Thanks for your interest in history, and for your patience.
> 
> Best wishes, Don Knuth
