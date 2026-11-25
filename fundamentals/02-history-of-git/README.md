# Linux, BitKeeper and the birth of Git

[English](README.md) · [Português](README.pt-BR.md) · [Español](README.es.md)

<!-- navigation -->
[Previous](../01-version-control/README.md) · [Index](../README.md) · [Next](../03-distributed-and-platforms/README.md)
<!-- /navigation -->

**Level:** beginner · **Estimated time:** 20 min

**Prerequisites:** [Why version control exists](../01-version-control/README.md)

**Objective:** Connect Git's origin to distributed development.

## What and why

Linux is a kernel, the core of an operating system. Linus Torvalds began Linux in 1991. From 2002 kernel developers used BitKeeper, a proprietary distributed version control system (VCS). The free-use arrangement ended in 2005, and Torvalds and other contributors developed Git for kernel work. Goals included speed, distributed work, parallel branches and handling a large project. Git is not Linux itself and works on Windows, Linux and macOS.

## Practice

Timeline: 1991 Linux starts; 2002 kernel developers use BitKeeper; 2005 Git starts. The reasons matter more than the dates.

In a fictional translation project, one contributor revises English and another Spanish. Both can record local history independently, then integrate when connected. No commands needed here.

## Common mistakes and safety

Do not confuse Git with later hosting platforms. Distributed development does not eliminate coordination or conflicts.

## Exercise and self-check

Explain why local history matters when network access disappears. Hint: local commits still work. Pass if you distinguish Linux (kernel), BitKeeper (earlier VCS) and Git (distributed VCS created in 2005).

## Quick reference

Connect Git's origin to distributed development.

## Official sources

- [https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git](https://git-scm.com/book/en/v2/Getting-Started-A-Short-History-of-Git)
