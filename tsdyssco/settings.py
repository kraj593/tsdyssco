class Settings:
    def __init__(self):
        self.k_m = 0
        self.substrate_uptake = 'generalized_logistic'
        self.parallel = False
        self.num_points = 50
        self.objective = 'productivity'
        self.initial_biomass = 0.05
        self.initial_substrate = 50
        self.initial_product = 0
        self.time_end = 20

settings = Settings()
