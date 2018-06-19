# Change log

This file describes major changes to NILMTK between versions.


## Development version (will become v0.3)

### New features

* [Ability to specify the number of states to use for modeling each appliance](http://nipunbatra.github.io/2015/07/nilmtk-states/)
* `MeterGroup.plot()`
* Correlation between different Elecmeters and corresponding plot; Issue #160
* Finding number of simultaneous appliance switches; Issue #163
* `CSVDataStore`
* Finding entropy of an ElecMeter. Issue #250
* `ElecMeter.plot_lag()`.  Issue #255.  See [Nipun's blog post](http://nipunbatra.github.io/2014/12/nilmtk-new-plots)
* `ElecMeter.plot_autocorrelation()`.  See [Nipun's blog post](http://nipunbatra.github.io/2014/12/nilmtk-new-plots)
* `ElecMeter.plot_spectrum()`.  See [Nipun's blog post](http://nipunbatra.github.io/2014/12/nilmtk-new-plots)
* Support for Python 3.6 and Pandas 0.22. Python 2.7 is still supported for the time being.

### New dataset converters

* AMPds
* COMBED
* ECO
* GREEND
* iAWE
* UK-DALE
* Dataport


### Disaggregation algorithms

* An implementation of George Hart's 1985 algorithm
* The combinatorial optimisation algorithm has received several
  updates including:
    * it takes the 'vampire power' into account during disaggregation

* Disaggregation output now includes basic metadata such as the
  appliance types.


### Performance improvements

* `HDFDataStore.load()` is more than 40 times faster than in v0.2.
  This function is called by pretty much every other function so this
  speed up should be felt throughout much of NILMTK.


### API changes

* `ElecMeter.total_energy()` and `MeterGroup.total_energy()` always
  returns a `pd.Series` if `full_results=False` (it used to return a
  scalar if the meter only had a single AC type, or a Series if there
  were multiple AC types).
* `HDFDataStore.append()` actually appends now!  (It used to
  `put`).  We now have separate `DataStore.append` and
  `DataStore.put` methods.


### Statistics

* `MeterGroup.proportion_of_energy_submetered()` does a better job
  of comparing AC types.


### Bug fixes

* `MeterGroup.proportion_of_energy_submetered()` has had multiple
  fixes.
* Lots of other bug fixes!


## v0.2


v0.2 was released on the 12th July 2014.

NILMTK v0.2 is a complete re-write of NILMTK from the ground up.

Some feature highlights of v0.2:

* The entire pipeline (loading, stats, preprocessing, disag, metrics)
  can cope with arbitrarily large datasets whilst being gently on the
  system RAM usage
* Full metadata support, including for arbitrary wiring hierarchies
* MeterGroup allows users to select and aggregate meters in powerful
  ways with a single line of code.  e.g. to see the total energy used
  by all the lights in a house just do
  'elec.select(category='lighting').total_energy()'.
* Much more elegant handling of "dual supply" and split-phase mains
  (using MeterGroup)
* Experimental support for preconditions checks for some stats
  function.
* OOP design hides complexity from the user
* CO works well
* Most metrics have been converted
* REDD converter works
* about 40 unit tests
* Disag output is now saved chunk-by-chunk to disk, allowing us to
  disag and do metrics on arbitrarily large datasets.  Also lays the
  foundation for sharing raw disag output and for users to be able to
  ignore all the NILMTK pipeline except the metrics
* Automatic selection of the best type of power measurement (reactive,
  active or apparent) etc etc...

However, there are still some things that are implemented in NILMTK
v0.1 but are not yet in v0.2.  For example:

* v0.2 does not yet include all the dataset importers that v0.1 had.
* v0.2 only has one disag algo: CO.  It should be fairly simple to
  port the FHMM algo from v0.1
* There are a few stats functions and metrics which we haven't had a
  chance to port.


## NILMTK v0.1

NILMTK v0.1 was released on Feb 7th 2014.
