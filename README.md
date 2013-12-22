learning-from-patient-safety-incidents
======================================

Dissertation submitted in partial fulfilment of the
Masters of Science in Health Informatics
University College London
December 2013

Learning from patient safety incidents: can data mining help?
=

Abstract
==

Background
===
To reduce preventable harm to patients health care professionals
report unexpected events that harm, or nearly harm, patients. In England and
Wales, the National Health Service (NHS) provides standardized patient safety
incident report forms for this purpose which are collated nationally by the National Reporting and Learning System (NRLS). To date over seven million patient
safety incidents have been reported to the NRLS. The magnitude of this dataset
presents a major challenge for the NRLS analytic team. Two key analytic tasks
are:
1. To group similar incidents in order to find common modifiable causes and
inform prevention strategies
2. To classify the severity of incidents occurring in order to prioritize and
target remedial efforts
Data Mining(DM), a process that includes the use of machine learning algorithms, is emerging as a useful analysis technique in a diverse range of endeavours
that involve large datasets. DM techniques are not yet routinely used in opera-
tional patient safety systems but they have shown promise as an analytic tool in
a variety of patient safety research settings.
It is not known whether DM could help the analysis work of the NRLS by,
for example, offering efficiency gains, supporting the existing work of analysts,
and permitting new insights into this large database. This is examined for a
subset of NRLS patient safety incidents that relate to computer use by testing
data exploration and auditing tools, the Lingo clustering algorithm, and Naive
Bayes (NB) and Stochastic Gradient Descent (SGD) incident severity classifiers.

Methods
===
A database extraction, transform, and load (ETL) approach was used
as a precursor to performing cluster analysis and building an incident severity
classifier.
Incidents reported as occurring between 1st January 2002 and 1st March 2012
and classified as concerning computer systems were extracted from the NRLS
database.
Data were cleaned and selected fields (incident free text description and severity of incident) were converted to csv and xml data formats for subsequent analysis
using Apache Solr, Scikit-learn and NLTK (csv), and Carrot2 (xml). Preprocessing techniques including stemming, tokenization, tagging, and filtering.
Extracted data were audited using Python Brewery and validated by searching
for known patterns of interest using Grep, Google Refine, and Apache Solr. Data
were loaded into NLTK for lexical analysis, Apache Solr to search for strings of
interest for validation, Carrot2 platform to perform cluster analysis, and Scikit-
learn in order to construct severity classifiers.
Lingo (a clustering algorithm based on singular value decomposition) was
employed within the Carrot2 platform to perform cluster analysis on selected
data. NB and SGD incident severity classifiers were tuned using a grid search
strategy and evaluated using cross validation.

Results
===
Between 1st January 2002 and 1st March 2012 7273 incidents were classified by NPSA staff as belonging to “Infrastructure (including staffing, facilities,
environment)” (incident category level 1) and “IT / telecommunications failure /
overload” (incident category level 2) categories. Incidents reported to have caused
no harm were the most common (n = 5982). Incidents causing death (n = 7) or
severe harm (n = 62) were less common. The detail provided by reporters when
describing incidents varied considerably. The median number of words in the free
text incident description field (IN07) was 25 and the range spanned 1-738 (this
was a mandatory field).
Evidence of poor systems reliability and problems not being fixed promptly
were identified as themes by manual search using Grep, Solr and NLTK. Being
unable to carry out a task because of computer systems failure, and problems
relating to hospital bleep system failure were identified as themes using the lingo
clustering algorithm.
Optimised NB and SGD incident severity classifiers performed similarly at
predicting incident severity class from free text incident descriptions. NB classifier: precision = 0.76, recall = 0.83, f1-score = 0.77. SGD classifier: precision =
0.78, recall = 0.84, f1-score = 0.77.

Conclusion 
===
DM can offer a valuable additional technique for the patient safety
analyst.
With the increasing digitisation of health care demonstration of utility may be
more easily obtained when reporting, expert analysis, and action are more closely
integrated into tighter feedback loops. For example a classifier used to predict
prescription error might be constructed and tied to a prevention intervention with
the goal of reducing the rate of a specific measurable harm occurring.
For the subset of patient safety incidents relating to computer use considered,
the application of DM methods suggests that the NRLS system does not result
in the timely resolution of safety issues. For safety incidents due to computer
problems, and possibly other types of safety incident, lessons might be learned
from more general approaches to, and cultures of, systems improvement. In
particular, the more open and action focussed approach to improving quality
present in bug reporting systems found in the open source software community
has intuitive appeal.
Key words Health Information Systems, Patient Safety, Artificial Intelligence,
Risk Management, Data Mining
