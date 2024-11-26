import numpy as np
import matplotlib.pyplot as plt


class SineSampleGen:
    """
    A sine sample generator. Instance frequency is constant.
    """

    def __init__(self, frequency: float, amplitude: float):
        """
        Construct a sine wave sampling object, which "stores" a sine wave of
        given frequency and amplitude.
        """
        self.frequency = frequency
        # How can a class own a sine wave?
        self.sine = lambda x: amplitude * np.sin(2 * np.pi * frequency * x)
        self.sine_val = None  # (like this?) to be used later

    def sample(self, frequency: float, time: float) -> tuple:
        """
        Sample self.sine with sampling frequency: @frequency
        over acquisition time: @time.
        Returns a tuple of sampled ([x_values], [y_values]).
        """
        x_val = np.linspace(0, time, int(1e5))
        self.sine_val = (x_val, self.sine(x_val))  # this is also sampling

        time_interval = np.arange(0, time, 1 / frequency)
        sampled_vals = (time_interval, self.sine(time_interval))
        return sampled_vals

    def sample2plot(self, frequency: float, time: float) -> tuple:
        """
        Sample self.sine with sampling frequency: @frequency
        over acquisition time: @time. Then plot against the
        sine wave "owned" by this instance (self).
        Forwards the return value of self.sample().
        """
        plt.figure(figsize=(16, 9))
        sampled_vals = self.sample(frequency, time)

        plt.plot(self.sine_val[0], self.sine_val[1],
                 label=f"Sine wave {self.frequency} Hz", color="orange")
        plt.scatter(sampled_vals[0], sampled_vals[1],
                    label="Sampled wave", color="blue", marker='.')

        plt.xlim(min(self.sine_val[0]), max(self.sine_val[0]))
        plt.grid(True, axis="both")
        plt.xlabel("Time [s]", fontsize=16)
        plt.ylabel("Amplitude", fontsize=16)
        plt.title(f"Sampled wave at rate {frequency} Hz vs original wave",
                  fontsize=20)
        plt.legend(loc="upper left", bbox_to_anchor=(1, 1), fontsize=12)
        plt.tight_layout()
        plt.show()
        return sampled_vals


freq = int(input("Type index number: ")) % 100
if freq == 0:
    freq = 1
ampl = float(input("Wave amplitude: "))
print(f"Sine wave will be of frequency {freq} Hz and amplitude of {ampl}")
generator = SineSampleGen(freq, ampl)
sample_rate = float(input("Sample rate [Hz]: "))
acquisition = float(input("Acquisition time [s]: "))
generator.sample2plot(sample_rate, acquisition)

