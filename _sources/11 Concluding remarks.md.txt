# 11. Concluding remarks

## 11.1 Conclusions

Generalised parsing is an important area of research. The incorporation of a GLR mode in GNU Bison, and the emergence of tools such as the Asf+Sdf Meta-Environment and Stratego/XT highlight the increasing practical importance of generalised parsing techniques. Unfortunately the generalised parsing algorithms used by such tools are still relatively inefficient. Although straightforward optimisations can significantly improve their performance, the literature lacks a comprehensive analysis of the different techniques, which hinders the understanding and improvement of existing approaches and hampers the development of new ideas.

This thesis advances the study of generalised parsing algorithms by providing the following contributions: a comprehensive, comparative analysis of generalised parsing techniques; a new tool, the Parser Animation Tool (PAT), which aids the understanding of the different techniques and can be used to compare their performance; and the BRNGLR algorithm, a new algorithm that displays cubic complexity in the worst case.

The theoretical treatment of the different generalised parsing techniques presented in this thesis is supported by the PAT. The implementation of the algorithms in PAT closely follows their theoretical description. In addition to graphically animating the algorithms' operation PAT collects statistical data which has been used to analyse their performance in Chapter 10. The main results of this work are as follows:

* Both variants of Farshi's algorithms perform poorly when compared to the other techniques.
* The performance of Farshi's algorithm is significantly improved by implementing the straightforward optimisation highlighted in Chapter 4.
* The RNGLR algorithm performs very well in comparison to all the other algorithms for all experiments.

* The BRNGLR algorithm performs an order of magnitude fewer edge visits than the RNGLR algorithm during a parse of a grammar which triggers worst case behaviour for both algorithms.
* The performance of the BRNGLR algorithm also compares very well to the RNGLR algorithm for the programming language parses.
* The performance of the RIGLR algorithm compares well to the BRNGLR and RNGLR algorithms. Additionally there is an order of magnitude reduction in the size of the structures constructed during a parse by the RIGLR algorithm when compared to the RNGLR and BRNGLR algorithms. Unfortunately the size of the RCA's for the programming language grammars is impractically large.

All of the tools which use a GLR parser that were inspected as part of this thesis implement the naive version of Farshi's algorithm. As the results in this thesis show, a significant improvement in performance can be achieved by making a relatively simple modification to this algorithm.

## 11.2 Future work

The contributions of this thesis advance the study of generalised parsing, but there are still several areas that can be significantly improved by further research. In the remainder of this chapter we briefly discuss some possibilities for future research in the field.

### Resolution of ambiguities

Theoretically speaking it is desirable for a generalised parser to produce all possible derivations of a parse, and the SPPF representation provides a relatively efficient structure to do this with. The problem, however, is that in practice most applications only want their parsers to output one derivation and extracting the desired parse tree from a forest is not usually straight forward. Ambiguities are often difficult to understand and modifying the grammar so as to remove them can result in more ambiguities being introduced and a less intuitive grammar.

New techniques need to be developed and incorporated into generalised parsers that simplify the selection of a single parse tree from a forest. The work done on disambiguation filtering [23] in scannerless GLR parsing is an interesting approach. The incorporation of such techniques in the existing GLR algorithms should not be difficult.

### Investigating the effect of the additional GSS nodes created by the BRNGLR algorithm

The theoretical analysis of the BRNGLR algorithm has shown that, in the worst case, it is asymptotically better than the existing GLR algorithms. Furthermore, the results in Chapter 10 indicate that it also performs well in practice. However, it would be interesting to investigate the actual runtime costs that are contributed by the additional nodes created in the GSS. Could the performance of the algorithm be improved in some cases by compromising its worst case complexity and only selectively creating additional nodes?

### Using the RIGLR algorithm to improve the performance of scannerless parsers

Scannerless (S)GLR parsers do not use a separate scanner to divide the input string into lexical tokens. Instead they incorporate the lexical analysis phase into the parser. Although this approach has its advantages, one of its main drawbacks is that it can be less efficient; "scanning with a finite automaton has a lower complexity than parsing with a stack" [20, p.36]. Perhaps the efficiency of SGLR parsers can be improved by partially incorporating the techniques developed for the RIGLR algorithm.

### Error reporting in GLR parsers

A common complaint against bottom-up parsing techniques in general, is what is considered to be their complicated error reporting. Deterministic bottom-up parsers such as Yacc often refer to parse table actions when a parse error is encountered. Although a considerable amount of research has been done on improving the error reporting for LR parsers, relatively little work has been done for GLR parsers.
