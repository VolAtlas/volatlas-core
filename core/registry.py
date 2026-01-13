class AssetRegistry:
    def __init__(self):
        self.assets = {}

    def register(self, symbol: str, metadata: dict):
        self.assets[symbol] = metadata

    def get(self, symbol: str):
        return self.assets.get(symbol, {})
