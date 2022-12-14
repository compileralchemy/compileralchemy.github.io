


<div class="chapter"></div>

<ul class="toc">
<li><a href="#foreword">Foreword</a></li>
<li><a href="#intro">Introduction</a></li>
<li><a href="#c1"><abbr title="HyperText Markup Language">The Story Behind</abbr></a></li>
<li><a href="#c2"><abbr title="HyperText Markup Language">Overview</abbr></a></li>
<li><a href="#c3"><abbr title="HyperText Markup Language">File & Record Format</abbr></a></li>
<li><a href="#c4"><abbr title="HyperText Markup Language">Functionalities</abbr></a></li>

</ul>
<div class="chapter"></div>

<h1 id="foreword">Foreword</h1>

To all SQLite lovers. You can view [compileralchemy.com](https://www.compileralchemy.com) or [contribute to the book](https://github.com/compileralchemy/compileralchemy.github.io/blob/master/data/books/sqlite_internals.md). It is OpenSource! Feel free to fix typos etc.

<div class="chapter"></div>

<h1 id="intro">Introduction</h1>


SQLite is a file-based database which is extremely reliable and stable. 
It is the world's most used database. 
The codebase and mechanisms it used is extremely complex. 
The seemingly simple nature of it and adoption makes a good case for deep diving into in a fascinating piece of software.

<h1 id="c1">Chapter 1: The Story Behind</h1>


SQLite was written by Dwayne Richard Hipp.
It is not uncommon to see it being abbreviated to D. Richard Hipp or DRH for short.
The story of how the database came around is fascinating.
It sheds light on the author's mindset and SQLite general coding culture.

DRH holds a computer science doctorate. Since his early days he was very dedicated. 
He dropped out of academia as the race was full of candidates.
He turned to consulting.
During that time, he was signed a software contract with shipyard _Bath Iron Works_. 
His work involved finding the solution to pipe burst failure by controlling valves on a warship: the _DDG-79 Oscar
Austin_.

![](../../assets/books/sqlite-internals/oscar_austin.jpg)

Richard had a problem.
The software often did not work as the database server was down all the time.
The ship was using _Informix_.
So, he thought of spinning his own database.


> one of the guys I was working with says, “Richard, why
> don’t you just write one?” “Okay, I’ll give it a try.

> ...

> all government contracts got shut down, so I was out of
> work for a few months, and I thought, “Well, I’ll just write
> that database engine now.”

Contrary to many popular projects, Richard thought of a bytecode-driven engine since the begining.
This shows his previous exposure to compiler crafstmanship.

> so I wrote a byte code engine that would actually run a
query and then I wrote a compiler that would translate
SQL into that byte code and voila, SQLite was born.

## How SQLite picked up speed

SQLite was not an overnight success though people did realise it's potential since the early days.
This is a list of some milestones which led to SQLite what it is today.


**2000 - The Internet:** Since the shipyard was adamant on _Informix_, SQLite was not used on the warship.
Robert put the code out in the wild on the internet.
One great moment was a personal initiative from a user running it on his _Palm Pilot_.

**2001 - Motorola OS:** Motorola was a phone manufacturing company. 
The operating system they were using had SQLite on it.
They wanted some help. 
During the whole time, Richard has been working on the project as an OpenSource one.
So, they proposed an $80k contract to Richard for support and enhancements.
It was the first time that the author realized that OpenSource can bring in money.
He rounded his OSS team and shipped the project.
This would be the first in a series of long-lasting relationship with phone companies.

**200x - America Online:** The next serious company to reach out was America Online.
They wanted the database on CDs they were mailing to customers. 
Richard enthusiastically accepted the offer and midway realized the solution he had in mind would not work.
These types of challenges helped SQLite grow into a robust product.

**200x - Symbian OS:** Symbian flew Richard to their office in London.
Among many databases they evaluated, both OSS and closed-source, SQLite was chosen.
Symbian was a great company but they had a problem. 
They wanted to ensure that the project lives on even if Richard is no longer around.
They wanted to increase the bus factor by having a SQLite consorsium.


**200x - SQLite Consortium:** Richard liked the idea of a consorsium.
He started devising a plan of his own.
Luckily someone from the Mozilla foundation reached out to him.
They did not like the way he was setting up the framework around the consorsium by giving members voting rights.
They proposed keeping the direction of the project in developers hand. 
The friend from Mozilla being a lawyer was adamant on this point and saw through the implementation of the current setup.

**200x - Google & Android:** Google was a complete outsider to the phone game.
Soon, they approached Richard for a daring project.
Having a phone connected to the internet with a robust software lifecycle was something extraordinary.
They wanted SQLite to behave perfectly on this innovation.
Richard's experience with the phone industry knew that Android was going to be a huge hit.

> We were going around boasting to everybody naively
> that SQLite didn’t have any bugs in it, or no serious bugs,
> but Android definitely proved us wrong. ... It’s amazing
> how many bugs will crop up when your software
> suddenly gets shipped on millions of devices.


**200x - Rockwell Collins:** Rockwell Collins was a multinational corporation providing avionics and information technology systems and services to government agencies and aircraft manufacturers.
They wanted the _DO-178B_ aviation quality standard for SQLite.
It meant 100% MCDC test coverage.
This helped shaped SQLite test-backed approach to development.


SQLite tests are better than even postgres which relies on peer reviews [3]. This allows the developers to experiment and change code fearlessly.


## A from scratch principle


SQLite is notorious for implenting a bunch of functionalities from scratch.
It's a daring, amazing, bold and crazy spirit which requires confidence and professionalism.
People also call it the _From First Principles_ approach.
With no internet at the tips of the fingers and no wikipedia to consult, the author deserves massive respect.
His teachers must have been proud to have their student be the living embodiment of what computer science and software engineering should be about.

DRH does look for alternatives. 
He does try out libraries.
But, at the end of the day he ends up coding from scratch.

First, he needed a database engine, he looked around, was not satisfied and went on to pull off his own implementation.

The same goes for the b-tree layer.
Much like a hero from a movie, he pulled Donald Knuth's algorithm book from the shelf and coded the b-tree he needed.
He also completed the book's exercise about deleting elements. 

He doesn't understand the use of YACC, Bison and Lex when anybody can code their own parsers.

He was using Git, but some functionalities were scratching his itch to build his own Control Version System. So, as usual, he wrote _Fossil_. 
It's the CVS you would download and configure if you download the source as is from the website.


> ... And it's GPL, and
> so SQLite Version 1 was GPL, it had to be because it
> was linking against the GPL library.
> But GDBM is only key-value, I can't do range queries
> with it. Then I said, “I'm gonna write my own B-tree
> layer


The from scratch spirit is much preferred as it enables the developers to have the freedom they want.
They can choose what they want or how they implement things.
Just wrapping over another library might be a problem waiting to happen.

We can expect the library to be fairly complex as there are several components present which require knoledge of their own.

> never understood lex because it's so easy to write a bunch of C codes faster then Lex [1]

<div class="chapter"></div>

<h1 id="c2">Chapter 2: Overview</h1>

A rough overview of SQLite is as follows


```

--------------     ------------
| SQLite lib |  ⇐  | SQL code |
--------------     ------------
	  ⇑ ⇓ 
---------------
| Binary file |
---------------
```

A brief overview of the compilation step is as follows.
The compiler takes the SQL code and outputs bytecodes.
The Virtual Machine (VM) takes the bytecode and executes it.

```
+----------+     +----------+     +----+
| Compiler | --> | bytecode | --> | VM |
+----------+     +----------+     +----+
```

## The compilation and execution process

A better view of the process might be 



```
  SQL
   |
   v
[ parser ]
   |
   v
[ code generator ] 
   |
   v
[ VM ]
   |
   v
[ btree ]
   |
   v
[ pager ]
   |
   v
[ shim ]
   |
   v
[ OS Interface ]
```

The first part of the library is called the compiler. 
It is executed using the `sqlite3_prepare_v2()` function and outputs prepared statements aka bytecodes.

```
[ parser ]          \
   |                 \ compiler 
   v                 /
[ code generator ]  / 
   |
   v
[ VM ]  
   |      
   v       
[ btree ] 
   |      
   v      
[ pager ]   
   |      
   v      
[ shim ] 
   |    
   v              
[ OS Interface ] 
```

The second part of the library runs the program. 
It is executed using the `sqlite3_step()` function.


```
[ parser ]         
   |               
   v               
[ code generator ] 
   |
   v
[ VM ]              \
   |                 \
   v                  \
[ btree ]              \
   |                    \ run the program
   v                    /
[ pager ]              /
   |                  /
   v                 /
[ shim ]            /
   |               /
   v              / 
[ OS Interface ] /
```

The btree layer and onward is called the storage engine.

```
[ parser ]       
   |               
   v               
[ code generator ]
   |
   v
[ VM ]             
   |                
   v               
[ btree ]        \           
   |              \             
   v               \          
[ pager ]           \         
   |                 \ storage engine
   v                 /
[ shim ]            /
   |               /
   v              /
[ OS Interface ] /
```

## Steps explanation


- **Tokeniser - Parser:** The parser is a push-down automaton parser.
It is reentrant and thread-safe. 
It is generated by lemon. Relevent files include `parse.y`, `tool/lemon.c`.
Outputs AST (`sqliteInt.h`).

- **Code generator:** It does semantic analysis. 
It does AST transformation using `select.c`.
It determines join order using `where*.c`, `whereInt.h`.
It does query planning using `select.c`.
It outputs bytecodes using `build.c`, `delete.c`, `expr.c`, `insert.c`, `update.c`.
It is the section with the most lines of code.

- **Virtual Machine:** It is the section with the 2nd most number of lines of code.
Relevant files includes `vdbe.c`, `vdbe.h`, `vdbeLnt.h`, `vdbe*.c`, `func.c`, `date.c`.
It executes bytecode instructions from the previous step.


```
[ parser ] 
   |
   v
[ code generator ]
   |
   v
[ VM ] 
   | Interface defined by btree.h
   v
[ btree ]
   |
   v
[ pager ]
   |
   v
[ shim ]
   |
   v
[ OS Interface ]
```

- **B-tree:** SQLite uses both B+ and B- trees. 
B+ tree is used for storing tables and B- is used for indexes.
There can be multiple btrees per database file.
It is read using a cursor.
Concurrent reads and writes on same table is done using different cursors.

- **Pager:** Also called page cache.
Prevents from data corruption in case of power loss.
It uses two mutually exclusive modes to achieve this.
The Roll back mode or the Write Ahead Log (WAL) mode.
It also enforces concurrency control.
It is responsible for dealing with in-memory cache.
Relevent files include `pager.c`, `pager.h`, `pcache1.c`, `pcache.c`, `pcache.h`, `wal.c`, `wal.h`.

- **Shim:** The Shim layer is responsible for compression, logging and encryption.
It is used to emulate an OS layer.
It is used for tests to simulate hardware failures.
Relevant files include `test_multiplex.c`, `test_vfstrace.c`


- **OS Interface:** It is used for os-specific interfacing. 
It can be changed at runtime.
It is responsible for I/O (`test_onefile.c`).
Relevant files include `os.c`, `os_unix.c`, `os_win.c`, `os*.h`. 


<div class="chapter"></div>
<h1 id="c3">Chapter 3: File & Record Format</h1>

A SQLite file is a series of bytes.


```
[b1 b2 b3 b4 b5 ...]
```

It is divided into equally-sized chuncks called pages. There can be one or more pages.


```
----------------------------------------------
| page 1 | page 2 | page 3 | page 4 | page 5 |
----------------------------------------------
```

The first page is the most important. 
It declares vital information about the file.
The first page looks like this.
The first 16 bytes contains the string `SQLite format 3`. 
In hex it is like this `53 51 4c 69 74 65 20 66 6f 72 6d 61 74 20 33 00`, including the null terminator at the end `\000`.

The next two bytes states the file size.
Before 3.7.0.1 it had to be between 512 and 32768.
As from 3.7.1 it can be of size 65536. 
Since such a large number cannot fit in 2 bytes, the value is set to `0x00 0x01`.
This represents big-indian 1 and is used to specify a size of 65536.


```
0                 16       18
------------------------------
| SQLite format 3 |  400   |
------------------------------
[                     page 1        ..
```

Here is a complete table about what the first page contains.

```
start byte - offset byte - description

00	16	The header string: "SQLite format 3\000"
16	02	The database page size in bytes. Must be a power of two between 512 and 32768 inclusive, or the value 1 representing a page size of 65536.
18	01	File format write version. 1 for legacy; 2 for WAL.
19	01	File format read version. 1 for legacy; 2 for WAL.
20	01	Bytes of unused "reserved" space at the end of each page. Usually 0.
21	01	Maximum embedded payload fraction. Must be 64.
22	01	Minimum embedded payload fraction. Must be 32.
23	01	Leaf payload fraction. Must be 32.
24	04	File change counter.
28	04	Size of the database file in pages. The "in-header database size".
32	04	Page number of the first freelist trunk page.
36	04	Total number of freelist pages.
40	04	The schema cookie.
44	04	The schema format number. Supported schema formats are 1, 2, 3, and 4.
48	04	Default page cache size.
52	04	The page number of the largest root b-tree page when in auto-vacuum or incremental-vacuum modes, or zero otherwise.
56	04	The database text encoding. A value of 1 means UTF-8. A value of 2 means UTF-16le. A value of 3 means UTF-16be.
60	04	The "user version" as read and set by the user_version pragma.
64	04	True (non-zero) for incremental-vacuum mode. False (zero) otherwise.
68	04	The "Application ID" set by PRAGMA application_id.
72	20	Reserved for expansion. Must be zero.
92	04	The version-valid-for number.
96	04	SQLITE_VERSION_NUMBER
```

Pages can be one of the following:


```
- The lock-byte page

- A freelist page -------A freelist trunk page
				    \
				     --- A freelist leaf page

- A b-tree page ------ A table b-tree interior page
				   \
				    --- A table b-tree leaf page
				    |
	                --- An index b-tree interior page
	                |
	                --- An index b-tree leaf page

- A payload overflow page
- A pointer map page
```

<div class="chapter"></div>
<h1 id="c4">Chapter 4: Functionalities</h1>