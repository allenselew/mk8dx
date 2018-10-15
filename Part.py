
'''
Base class for racers, karts, wheels and gliders.
'''

class Part():
    def __init__(self, name,
        weight, acceleration, on_road_traction, off_road_traction,
        mini_turbo, ground_speed, water_speed, antigravity_speed, air_speed,
        ground_handling, water_handling, antigravity_handling, air_handling):
        self.name = name
        self.weight = weight
        self.acceleration = acceleration
        self.on_road_traction = on_road_traction
        self.off_road_traction = off_road_traction
        self.mini_turbo = mini_turbo
        self.ground_speed = ground_speed
        self.water_speed = water_speed
        self.antigravity_speed = antigravity_speed
        self.air_speed = air_speed
        self.ground_handling = ground_handling
        self.water_handling = water_handling
        self.antigravity_handling = antigravity_handling
        self.air_handling = air_handling
    
    def __add__(self, other):
        name = self.name + "-" + other.name
        weight = self.weight + other.weight
        acceleration = self.acceleration + other.acceleration
        on_road_traction = self.on_road_traction + other.on_road_traction
        off_road_traction = self.off_road_traction + other.off_road_traction
        mini_turbo = self.mini_turbo + other.mini_turbo
        ground_speed = self.ground_speed + other.ground_speed
        water_speed = self.water_speed + other.water_speed
        antigravity_speed = self.antigravity_speed + other.antigravity_speed
        air_speed = self.air_speed + other.air_speed
        ground_handling = self.ground_handling + other.ground_handling
        water_handling = self.water_handling + other.water_handling
        antigravity_handling = self.antigravity_handling + other.antigravity_handling
        air_handling = self.air_handling + other.air_handling

        return Part(name, weight, acceleration, on_road_traction, off_road_traction,
            mini_turbo, ground_speed, water_speed, antigravity_speed, air_speed,
            ground_handling, water_handling, antigravity_handling, air_handling)
