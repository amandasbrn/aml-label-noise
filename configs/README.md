# Configuration plan

Create separate, explicit configurations for Fashion and CIFAR after the smoke
pipeline works. Record at least:

- dataset path and exact filename;
- split seed;
- model settings;
- preprocessing settings;
- optimizer and learning rate;
- batch size;
- maximum epochs and patience;
- loss epsilon and documented weight handling;
- pilot-stage settings;
- revision-stage settings;
- device request;
- smoke/final marker;
- output directory.

Defaults are project choices, not automatically the paper authors' settings.
