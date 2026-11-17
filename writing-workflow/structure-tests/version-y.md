# Introduction

This synthetic study compares two models answering count questions, with and without a data dictionary. The question is whether the dictionary changes correctness on the tested questions. Correctness is evaluated against exact expected counts, not textual similarity.

# Methods

## Cases and expected counts

Four cases use fixed tables of records. For each case, the expected count is the number of rows satisfying the question's stated filter. A case with records marked true, true, false, true has expected count 3 when the question asks for true records. Neither model can read the expected counts.

## Generation

Each model receives the same question and tables. Each case is run once in each condition. The only changed input is access to the dictionary. This produces four answers for each of the four model/condition combinations. Each answer contains one integer count.

## Evaluation procedure

### Read the answer

A valid integer is required. Invalid or missing answers receive FAIL. A valid integer proceeds to the comparison below.

#### Compare with the expected count

The comparison uses the expected count defined in the cases section.

##### Assign the status

The status follows the rule in the next subsection.

###### Numerical rule and example

The two integers are evaluated and a status is assigned. The resulting statuses are used in the next subsection.

## Summarize the comparison

For each model/condition combination, divide the number of PASS answers by four and report the percentage. Report the per-case statuses alongside the percentage. These summaries measure correctness on the four tested cases.

# Results

The four combinations respectively obtain 4/4, 3/4, 4/4, and 2/4 PASS. Both models obtain 4/4 with the dictionary. Their results without it are 3/4 and 2/4. These counts do not establish a general guarantee for other tasks.

# Conclusion

Both models answer more of these four questions correctly with the dictionary. Further testing would be needed to establish performance on other data or questions.
