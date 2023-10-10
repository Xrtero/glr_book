# 1.1 Motivation

Most programming languages are implemented using almost deterministic context-free grammars and an LALR(1) parser generator such as Yacc, or GNU Bison. This approach to language development has been accepted for a long time and consequently many people believe that research into parsing is 'done'. This view is somewhat surprising given that there are still many important questions that remain unanswered. For example, the following two problems set by Knuth in his seminal paper [12] are still unsolved:

- Are there general parsing methods for which a linear parsing time can be guaranteed for all grammars? 

- Are there particular grammars for which no conceivable parsing method will be able to find one parse of each string in the language with running time at worst linearly proportional to the length of the string?

Clearly a lot more research needs to be carried out before we can honestly claim that parsing is 'done'. This thesis makes a significant contribution to _generalised_ parsing theory, specifically focusing on Tomita's GLR technique and its extensions.

A generalised parser is a parser that is capable of parsing strings for any context-free grammar. Although the first generalised parsing algorithms were published as far back as the 1960s, they have not generally been used in practice due to their relatively high runtime costs. The relentless improvement of computing power and storage, however, has seen interest in generalised parsing techniques resurface.

One of the main reasons behind the increased usage of generalised parsing is the popularity of languages like C++ that are difficult to parse using the standard deterministic techniques. Another is the increasing importance of software re-engineering tools that perform transformations of legacy software. Often this type of software is written in a programming language whose grammar is ambiguous.

Despite this increase in use, generalised parsers are still relatively inefficient; the most efficient generalised parsing algorithm to date displays $O(n^{2.376})$ complexity. Although it is believed that linear time generalised parsers are unlikely to exist, work should continue on improving the efficiency of generalised parsers. Unfortunately, the existing literature lacks a comprehensive, comparative analysis of generalised parsing techniques. This hinders the understanding of existing techniques and hampers the development of new approaches.

# 1.2 Contributions

The main contributions of this thesis are the description of the new Binary Right Nulled GLR (BRNGLR) parsing algorithm, the comparative analysis of existing GLR techniques and the development of the Parser Animation Tool (PAT).

PAT is a Java application that graphically displays and animates the operation of GLR parsing algorithms and collects statistical data that abstracts their performance. I implemented six different generalised parsing algorithms and several variants of each approach. The implementations closely follow the algorithms' theoretical description in the thesis. I used PAT to collect statistical data for each of the implemented algorithms and compiled a comparative analysis between the different approaches. This analysis indicates that the performance of parsing techniques adopted by several existing tools can be significantly improved by incorporating simple modifications described in this thesis.

The _BRNGLR_ algorithm is a new parser that displays cubic worst case complexity. Unlike other approaches that achieve cubic complexity the BRNGLR algorithm does not require its grammars to be modified and it constructs a representation of all derivations (during a parse) in at most cubic space. Although the initial idea of the algorithm is due to Scott, I was heavily involved throughout the development of the algorithm. In particular, I developed the prototype of _BRNGLR_ in PAT which was used to analyse the algorithms behaviour and test several optimisations.

In summary, the main contributions of this thesis are as follows: the presentation of the BRNGLR algorithm; the comprehensive analysis and description of existing GLR algorithms; new results which show that the techniques adopted by several existing tools can be significantly improved; and the Parser Animation Tool which provides a way of repeating and understanding the experiments and algorithms presented in this thesis.

Several of the results developed in this thesis have been subsequently published. The relevant papers are listed in the bibliography [JSE04a, JSE04b, JSE04c, JSE].

# 1.3 Outline of thesis

The thesis is split into four parts. Part I is made up of three chapters and provides the reader with the theory that is required in the rest of the thesis. Chapter 2 focuses on theory related to the specification and parsing of computer languages. Chapter 3 paints a picture of the major developments in generalised parsing and discusses relations between the various techniques. Chapter 4 introduces Tomita's GLR parsing algorithm and Farshi's later correction. A detailed discussion is given of both approaches highlighting some of their drawbacks.

Part II introduces three recent algorithms that use a variety of techniques to improve on the efficiency of the traditional GLR parsing algorithm. Chapter 5 describes the RNGLR algorithm that corrects Tomita's original algorithm by redefining the reduce action in the parse table. In addition to recasting the algorithm in terms of Rekers' SPPF representation, some modifications are proposed which improve its efficiency. Chapter 6 introduces the BRNGLR algorithm; a cubic-time parser based on the RNGLR algorithm that does not require any modification to be made to the grammar. Chapter 7 presents the RIGLR algorithm that attempts to improve the efficiency of a GLR algorithm by reducing the amount of stack activity. Chapter 8 discusses other work that has contributed to the development of generalised parsing, and relates them to the techniques described in this thesis.

Part III contains two chapters. Chapter 9 discusses some of the major applications of GLR and backtracking parsing techniques. As part of the work for this thesis, the algorithms discussed have been implemented in the Parser Animation Tool (PAT). This tool has been used to investigate the practical and theoretical strengths and weaknesses of the algorithms. In parallel, the GTB tool has also been developed. Together, PAT and GTB have been used to run the algorithms on grammars for Pascal, C, Cobol and various smaller test grammars. The results are presented and discussed in Chapter 10.

Part IV contains one chapter that concludes the thesis and maps out possible future work.