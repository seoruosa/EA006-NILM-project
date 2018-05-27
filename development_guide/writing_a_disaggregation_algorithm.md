# Writing a disaggregation algorithm

Disaggegration algorithms in NILMTK reside in the
`nilmtk/nilmtk/disaggregate/` directory and are implemented as python
classes. Each algorithm should extend the `Disaggregator` superclass,
and implement all required methods. Algorithms should implement
lazy-loading functionality via the `train_on_chunk` and
`disaggregate_chunk` methods. Algorithms should specify whether they
support supervised and/or unsupervised training. See the
`CombinatorialOptimisation` algorithm for a simple implementation of
the `Disaggregator` superclass.

In the `__init__` function, set `self.MODEL_NAME` to a short string
describing your algorithm.  e.g. we use 'CO' for combinatorial optimisation.

## Training

Disaggregation algorithms need to learn a model of how appliances consume energy from existing data. Such algorithms generally require appliance-level data from either the building which will be disaggregated (sometimes referred to as supervised) or buildings other than the one which will be disaggregated (sometimes referred to as unsupervised). The `train()` method should expect a `MeterGroup` object to be passed as a parameter containing a list of `ElecMeter` objects. Algorithms should specify if a `site_meter` is also required to be present in the `MeterGroup` object. This method is expected to iterate over chunks of data, passing each chunk to the `train_on_chunk()` method. The resulting learned method will be stored in memory as instance variables to the subclass. Subclasses should specify whether successive calls to the `train()` method either update or replace the existing model, while successive calls to `train_on_chunk()` should always update the existing model (rather than replacing it).

## Model loading and saving

The models learned via `train()` are held in volatile memory, and therefore will be lost once the disaggregator object has been destroyed. Persistent models can be implemented via the `import_model()` and `export_model()` methods, which will load a model from disk (replacing any in-memory model) and save an in-memory model to disk respectively. This allows learned models to be applied to large numbers of buildings without repeating the training process, and also the sharing of learned models amongst the research community. Models can be saved to disk in any format.

## Disaggregation

A disaggregation algorithm should use a learned model to separate a `site_meter`'s load into individual appliances. As with training, the `disaggregate()` method should iterate over chunks of aggregate data, calling `disaggregate_chunk()` on each chunk. The `disaggregate_chunk()` method should return a pandas dataframe, where the columns correspond to individual appliances and the rows correspond to instants in time. The returned dataframe's indexes should exactly match that of the dataframe received as a parameter. The `disaggregate()` method should save each disaggregated chunk to disk via the `datastore.append()` method, along with the required metadata. In addition to the disaggregated appliances, the method should also copy the aggregate data to the new datastore.
