# Asteroids
Clone of 1979 Atari game implemented with Pygame.

## Setup
Clone repository and in `Asteroids` directory type:
```bash
conda env create -f environment.yml
```

## Usage
In `Asteroids` directory type:
```bash
conda activate Asteroids
python -m Asteroids
conda deactivate
```

## Controls
Use `arrows` to move ship and `space` to shoot. You can pause the game with `P` and exit the game with `Esc`.

## Screenshots
![Title screen](screenshots/title_screen.png)
![Game screen](screenshots/game_screen.png)

## Development

### Guide
Commit messages are structured in accordance with:
- Write the summary line and description in the imperative mode. Start the line with "Fix", "Add", "Change" instead of "Fixed", "Added", "Changed".
- Always leave the second line blank.
- Don't end the summary with a period.

### Code analysis
Code analysis is performed with __Pylint__. To run it type:
```bash
pylint Asteroids/
```

## Attributions
> [Vector Battle](https://www.dafont.com/vector-battle.font) by [Freaky Fonts](https://www.dafont.com/freaky-fonts.d137)

> [Asteroids Sounds](http://www.classicgaming.cc/classics/asteroids/sounds) from [classicgaming.cc](http://www.classicgaming.cc/)

> [Asteroid B Icon](http://www.iconarchive.com/show/arcade-saturdays-icons-by-mad-science/Asteroid-B-icon.html) by [MadScienceLabs How](http://www.iconarchive.com/artist/mad-science.html)
