---
title: "Section 4 - Wordle"
author: Jed Rembold and Eric Roberts
date: "Date"
slideNumber: true
theme: monokai
highlightjs-theme: monokai
width: 1920
height: 1080
transition: fade
css:
  - css/codetrace.css
  - css/roberts.css
---


## Problem 1
- Everyone has experienced the drama of being forced to generate a new password with certain characteristics
- Here, your goal is to make use of the random library to generate a password of an arbitrary length and using a selection of characters
- Write a function `generate_password(length, chars)` which takes two arguments:
  - The length of the desired password as an integer
  - The string of possible characters to generate the password from
- Your function should _return_ the final password as a string


## Problem 2
- Interacting with the `WordleGWindow` object is mandatory in the Wordle project as a means to control or get information from the graphical window
- Displaying or reading information from the graphical squares generally requires referencing an index for both the column and row

## Turn that frown...
::::::cols
::::col
- For the first part of this problem, add code to the existing template so that when the program is immediately run, the Wordle squares form a frowing face as shown to the right
- For the square color, you can just use the string `"black"` (or choose any other fun color!)

::::

::::col
![Sad Wordle](./images/wordle_sad.png)

::::
::::::

## Upside Down!
::::::cols
::::col
- Now add code to the `enter_action()` function so that, then the `Enter` or `Return` key is pressed, the sad face turns into a smiley face
- You don't need to change **ALL** of the squares here, so just change the ones that you need to
::::

::::col
![Happy Wordle!](./images/wordle_happy.png)
::::
::::::


## Problem 3: Coloring
