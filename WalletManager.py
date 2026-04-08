import os
from web3 import Web3
from eth_account import Account
import secrets

# Konfigurera anslutning till Arbitrum (via en publik RPC)
RPC_URL = "https://arb1.arbitrum.io/rpc"
w3 = Web3(Web3.HTTPProvider(RPC_URL))

def initialize_agent_wallet():
    print("🤖 Sentinel Zero: Initierar autonom plånbokshantering...")
    
    # Generera en helt ny, säker privat nyckel
    priv_key = "0x" + secrets.token_hex(32)
    acct = Account.from_key(priv_key)
    
    print(f"✅ Ny EOA skapad!")
    print(f"📍 Offentlig adress: {acct.address}")
    print("⚠️  Denna adress har lagts till i din miljö. Skicka 0.002 ETH (Arbitrum) hit för gas.")

    # Spara adressen i .env för siktbarhet, men håll nyckeln redo för botens logik
    env_path = ".env"
    with open(env_path, "a") as f:
        f.write(f"\n# WA-21 Sentinel Zero Wallet\n")
        f.write(f"SENTINEL_ADDRESS={acct.address}\n")
        f.write(f"SENTINEL_PRIVATE_KEY={priv_key}\n")

    if w3.is_connected():
        balance = w3.eth.get_balance(acct.address)
        print(f"💰 Aktuellt saldo: {w3.from_wei(balance, 'ether')} ETH")
    else:
        print("❌ Kunde inte ansluta till Arbitrum-nätverket.")

if __name__ == "__main__":
    initialize_agent_wallet()
