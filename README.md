# Effect of heuristic post-processing on knowledge graph profile patterns

Experiment for the effect of heuristic post-processing on knowledge graph profile patterns with ABSTAT.

```commandline
Abstract: Sets of frequent schema-level patterns characterizing a given knowledge graph (KG) represent a central
output of profiling tools such as ABSTAT, as they could provide a quick overview of the coverage of the KG
and its adequacy for various tasks. However, the number of patterns may be huge. The most frequent ones are
not useful for semantically characterizing the KG since they feature generic (OWL, SKOS, etc.) classes and
even XML data types. We hypothesize that the pattern profile suitability for a `rapid skimming' scenario might
be improved by applying a machine learning (ML) method with a stop-list of namespaces or individual schema IRIs
by which the original pattern set is pruned. We experimented with post-processing the patterns returned by ABSTAT
concerning reducing the number of patterns and re-ranking the patterns appearing in the first positions of the
frequency-ordered results.

```


## Prerequisites

We require a Python version `3.7`.

Requirement by service:

| Service                    | Requirement(s)    |
|----------------------------|-------------------|
| ``          | `` |

## How to run

### With ``docker-compose``


```commandline

```

### Manually

```commandline


```


### Research paper:
```commandline
Title: `Effect of heuristic post-processing on knowledge graph profile patterns`
Authors: `Gollam Rabby, Farhana Keya, Vojtěch Svátek, Blerina Spahiu`
Conference: ProLingKNOWER 2023: PROfiling LINGuistic KNOWledgE gRaphs, Vienna, Austria, September 12-15, 2023
```
