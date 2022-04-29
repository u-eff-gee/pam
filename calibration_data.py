# This file is part of pam.

# pam is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# pam is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with pam.  If not, see <https://www.gnu.org/licenses/>.

class Calibration:
    """Class for storing all runs in a calibration experiment
    
On initialization, the array of runs passed to the Calibration class will be sorted.

Attributes
----------
identifier: string
    Identifier of the calibration experiment.
runs: array of Run objects
    Runs associated with the experiment.
    """
    
    def __init__(self, identifier, runs):
        self.identifier = identifier
        self.runs = sorted(runs)

class Run:
    """Class for storing all the information about a calibration run
    
For many of the parameters, the user can put in a continuous probability distribution from scipy.stats to take into account the uncertainty.
    
Attributes
----------
identifier: string
    Identifier for a run.
attenuator_dz: float or scipy.stats.rv_continuous
    Total thickness of the attenuators in cm.
MPAD_counts: float or scipy.stats.rv_continuous
    Total number of counts of the MPAD.
time: float or scipy.stats.rv_continuous
    Time interval in which the counts were recorded (assumed to be the same for all detectors).
MPAD_background_counts: float or scipy.stats.rv_continuous
    Total number of background counts of the MPAD.
background_time: float or scipy.stats.rv_continuous
    Time interval in which the background counts were recorded (assumed to be the same for all detectors).
MOLLY_counts: float or scipy.stats.rv_continuous
    Total number of counts of MOLLY.
MOLLY_efficiency: float or scipy.stats.rv_continuous
    Efficiency of MOLLY as the ratio between the number of incoming photons and the number of recorded events.
MOLLY_dead_time: float or scipy.stats.rv_continuous
    Dead time of MOLLY during the calibration run.
MOLLY_background_counts: float or scipy.stats.rv_continuous
    Total number of background counts of MOLLY.
    """
    def __init__(self, identifier,
                 attenuator_dz,
                 MPAD_counts, time,
                 MPAD_background_counts, background_time,
                 MOLLY_counts, 
                 MOLLY_efficiency, MOLLY_dead_time,
                 MOLLY_background_counts
                ):
        self.identifier = identifier
        self.attenuator_dz = attenuator_dz
        self.MPAD_counts = MPAD_counts
        self.time = time
        self.MPAD_background_counts = MPAD_background_counts
        self.background_time = background_time
        self.MOLLY_counts = MOLLY_counts
        self.MOLLY_efficiency = MOLLY_efficiency
        self.MOLLY_dead_time = MOLLY_dead_time
        self.MOLLY_background_counts = MOLLY_background_counts
        
    # Implement methods to sort the runs 
    def __lt__(self, other):
        return self.attenuator_dz.mean() < other.attenuator_dz.mean()

    def __le__(self, other):
        return self.attenuator_dz.mean() <= other.attenuator_dz.mean()
    
    def __gt__(self, other):
        return self.attenuator_dz.mean() > other.attenuator_dz.mean()

    def __ge__(self, other):
        return self.attenuator_dz.mean() >= other.attenuator_dz.mean()
    
    def __eq__(self, other):
        return self.attenuator_dz.mean() == other.attenuator_dz.mean()
    
    def __neq__(self, other):
        return self.attenuator_dz.mean() != other.attenuator_dz.mean()
