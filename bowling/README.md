# Bowling

## Expectations

- Test as you go
- Solve the problem iteratively
- Call out any refactors you are considering along the way and why

## Scoring

- 1 point per pin, dashes (`"-"`) are gutter balls
- **Spare** ( `[N, "/"]` ): 10 points + value of next shot
- **Strike** ( `["X", "-"]` ): 10 points + sum of the values of the next 2 shots
- In the 10th frame, if the first bowl is a strike, you get 2 more rolls
- In the 10th frame, if the second bowl is a spare, you get 1 more roll
- The score for the 10th frame is the total number of pins knocked down in the 10th frame.

