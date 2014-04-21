Protein Dynamics
===

These directories contain time series data for individual protein molecules structurally fluctuating in real-time. Each directory contains data for a separate unique condition for a common protein of interest. 

Each *.json file within each directory is the time series for a single molecule. Data acquisition occurred by recording on a camera the amount of light emitted by a single molecule. The time series are the result of extracting the light intensity fluctuations over time. 

The 'x' key in an individual *.json file is the time coordinate. The 'y' key is the light intensity coordinate. The light intensity coordinate maps to a three element vector containing the intensity values for three separate channels. The channels are determined by emitted wavelength. The first channel is a short emission wavelength channel (yellow light); the second is a long emission wavelength channel (red light); and the third is also the same long emission wavelength channel (red light), but stems from a different process. The first two channels are correlated. Ideally, the third channel is independent of the first two.

For more information concerning the unique nature of the data, data acquisition, and any peculiarities, consult references documenting single-molecule Forster resonance energy transfer (FRET). At the current time, no resources are easily found freely on the web explaining the concept well for those outside the field. (Alas, scientists are not the best at public relations!) One brief overview is provided by a group at the <a href="http://bio.physics.illinois.edu/newTechnique.html" target="_blank">University of Illinois</a>. If your instutition has an academic license for science journals, your attempts to find quality resources will be easier.