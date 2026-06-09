title: Opensource: Author's vision v/s Product's vision
---
Linus Benedict Torvalds started Linux as an educational project to learn more about the i386 microprocessor. It was based on the educational operating system called Minix. Like many opensource projects, many people have questioned Linus' engineering choices on various topics. Like Jose Crespo mentioned today concerning interrupt handling in RISC-V where they operate in a serial manner where each interrupt is processed sequentially.

But, questioning Linus starts right from the inception of Linux itself by none other than the creator of Minix, Andy Tanenbaum. Minix used a microkernel approach, where the userspace and kernel are separated. Linux used a monolithic approach. Andy told Linus in exasperation that \"While I could go into a long story here about the relative merits of the two designs, suffice it to say that among the people who actually design operating systems, the debate is essentially over. Microkernels have won.\"

Being on the research side of things, Andy labeled Linus' approach as pure misguidance. He accused him of catapulting us back to prehistoric ages: \"LINUX is
a monolithic style system. This is a giant step back into the 1970s. That is like taking an existing, working C program and rewriting it in BASIC. To me, writing a monolithic system in 1991 is a truly poor idea.\" 

And to that Linus agreed. From a theoretical point of view, he chose a bad design, but, he argued, Minix did not implement microkernels correctly. He preferred something that he could make to work well. 

There is always this rift in hashtag#opensource between the original author's wishes and basically everybody else. The original author often has the project's wellness and survival at heart. While people might be quick to judge and point out validly, the original author considers things holistically. A certain way of doing might be better but, the original author might prefer ease of use over doing things the right way. The original author has in addition, the vision behind the product.

But, of course, Linus is mortal. So, how do we keep the original author's vision, intentions, and definition around? It depends on the author, how much he taught about himself to others, and how much of the relationship between himself and the carving process he exposed to the world.

That's why many authors prefer to remain a dictator over the project, to guide the project to their dreams, not to a dream guided by the weathering process of maintainers' majority votes.
