# Decibel Values

- Source: https://plus4world.powweb.com/plus4encyclopedia/500288
- Category: Programming/Audio, Programming/General
- Keywords: amplitude, volume, decibel

The lower nibble (lower 4 bits) of TED register number 17 ($FF11) controls the overall volume of the audio output. The effective output volume levels range from no output (0) to maximum volume (8) in 9 steps. Writing values of 9-15 in the lower nibble are identical to selecting the maximum volume level (8).

The available volume levels correspond to the decibel values below.

| Volume | Decibel Value | Notes |
|---|---|---|
| 15 | 0.0 |  |
| 14 | 0.0 |  |
| 13 | 0.0 |  |
| 12 | 0.0 |  |
| 11 | 0.0 |  |
| 10 | 0.0 |  |
| 9 | 0.0 |  |
| 8 | 0.0 | (Maximum volume) |
| 7 | −1.2 |  |
| 6 | −2.5 |  |
| 5 | −4.1 |  |
| 4 | −6.0 |  |
| 3 | −8.5 |  |
| 2 | −12.0 |  |
| 1 | −18.1 | (18.1 dB down from the volume at maximum level) |
| 0 | Minus infinity |  |

Note: The decibels are shown as negative values from a maximum of 0.
