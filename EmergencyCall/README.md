# Transcribing an Emergency Call

## Introduction
Imagine you are working with an emergency response team to respond to 911 calls as quickly as possible.  One of the biggest problems the team faces is handling the transcription of the names of callers.  You've noticed that sometimes the name is misheard by the person taking the call, sometimes it is simply mistyped, and sometimes both.  These problems make it more difficult to search the database of DMV records to identify and locate the individual in need.

You would like to help solve this problem, and ensure the fastest response rates possible to help those in need.  You have read and write access to the list of transcribed names and the database of DMV records.  We need a way to effectively translate names based on their transcriptions and be able to narrow our search results to the one individual whose location we are interested in

## Input
You will receive a string array representing the list of transcribed names.
Each string in the array takes the following form:
+ The string will contain a first name and last name separated by a space.
+ You can assume every name has a capitalized first letter of the first name and capitalized first letter of the last name; no other letters will be capitalized.
You will also receive a string array representing the database of DMV records.
+ Each string will be of the form **Name**;**Address** (name string and address string separated by a semicolon).
+ As above, the name half of the string will contain a capitalized first name and a capitalized last name separated by a space.
+ The address half of the string will contain words with integers and characters in the standard English alphabet separated by spaces.
+ There will be no semicolons anywhere in the name or address strings.
You may also make the following assumptions about the structure:
+ No names will contain characters outside the standard English alphabet; this includes apostrophes and hyphens.
+ There will be at most 500 names in the DMV database.
+ There will be at most 50 names in the input.
+ No names will be repeated in either the input or the database.

## Output
For each transcribed name in the input string array, you want to match that to a name (first part of a string) in the DMV database.  The second part of the string in the DMV database will represent the address at which the person can be found according to the DMV records.  Your output should also be a string array, this time representing the addresses mapped to the names in the input string array.  You may assume that every input name will match a name in the DMV records.

## Responding to Calls

### The Basics
Let's start with the first step: making sure that if the name is transcribed perfectly, we match that person's record in the database right away.  This will give you an idea of how to match names in our system and what the output array should be.  This will also show you how the input is structured if you desire to make your own custom inputs.  The input comes in the form of two string arrays, where the first line represents the length of the array.  An example is below.

#### Input
```
3
Courtney Mackstutis
Angela Gimbel
Hector Koba
3
Courtney Mackstutis;4766 Moctezuma
Angela Gimbel;1270 Finazzo
Hector Koba;7074 Turrill
```

#### Output
```
["4766 Moctezuma", "1270 Finazzo", "7074 Turrill"]
```

Your code should pass tests 1, 2, and 3 after solving this step.

### Misspellings
The second thing we want to look for are basic misspellings due to the transcriber hearing the name correctly but missing a keystroke or pressing the wrong key instead.  Think "Shelby Sylvester" turns into "Shelvy Silvester" or "Ginette Carlock" turns into "Ginete Carloclk".  In the first example, the transcriber missed the "b" key and hit "v" instead, and missed the "y" and hit "i" instead.  In the second example, the transcriber accidentally missed a letter in the first name and added an additional one in the last name.  You should pass test cases 4 through 9 after solving this problem.  Hint: the phrase "string edit distance" should be of some help to you here.

#### Input
```
3
Courtnet Mackstutis
Angela Gimbrel
Hector Kba
3
Courtney Mackstutis;4766 Moctezuma
Angela Gimbel;1270 Finazzo
Hector Koba;7074 Turrill
```

#### Output
```
["4766 Moctezuma", "1270 Finazzo", "7074 Turrill"]
```

### Metaphones
The last and trickiest instance of transcription come in the form of arbitrary misspellings resulting from the transcriber either hearing the name correctly and using a different spelling than the one in our database, or mishearing the name in some form.  Think "Ashley" vs. "Ashlee" vs. "Ashleigh" or "Henry David Thoreau" turns into "Henney David Surrow".  This is a purposefully very open-ended and tricky problem, and you are not expected to get all cases.  One example is viewable and most are purposefully hidden - try to be creative with your solution, as there are multiple ways you could solve this piece!  Test cases 10 through 17 are the ones that relate to this part of the problem; as before, an example is below.

#### Input
```
3
Kourtnie Makstuttis
Anjelica Gimbell
Hector Cobrah 
3
Courtney Mackstutis;4766 Moctezuma
Angela Gimbel;1270 Finazzo
Hector Koba;7074 Turrill
```

#### Output
```
["4766 Moctezuma", "1270 Finazzo", "7074 Turrill"]
```
