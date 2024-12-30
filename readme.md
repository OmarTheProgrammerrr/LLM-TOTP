# LM_TOTP

## Overview
The `LM_TOTP` class provides a novel approach to generating Time-based One-Time Passwords (TOTP) by integrating GPT-2, a machine learning model, into the process. This method adds an additional layer of complexity and customization to traditional TOTP systems.

---

## Features
- **Dynamic Key Generation**: Uses GPT-2 to dynamically generate keys for TOTP.
- **Customizable Time Step**: Supports adjustable time intervals for TOTP expiration.
- **Validation**: Includes functionality to validate TOTPs against the generated ones.

---

## Installation

### Prerequisites
Make sure you have the following libraries installed:
- `transformers`
- `torch`
- `pyotp`
- `time`, `base64`, `hmac`, `hashlib`, `struct`, `secrets` (standard Python libraries)

Install required libraries using pip:
```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Import the Class
```python
from lm_totp import LM_TOTP
```

### 2. Initialize the Class
```python
secret = "MY_SECRET_KEY"
lm_totp = LM_TOTP(secret)
```

### 3. Generate a TOTP
Generate a TOTP for the current time:
```python
current_totp = lm_totp.now()
print("Current TOTP:", current_totp)
```

Generate a TOTP for a specific timestamp:
```python
specific_timestamp = int(time.time())
specific_totp = lm_totp.at(specific_timestamp)
print("TOTP for Specific Timestamp:", specific_totp)
```

### 4. Validate a TOTP
```python
given_totp = "123456"
is_valid = lm_totp.validate(given_totp)
print("Is Valid:", is_valid)
```

---

## Class Methods

### `__init__(self, secret, time_step=120)`
Initializes the LM_TOTP class.
- **Parameters**:
  - `secret` (str): The base secret key.
  - `time_step` (int): Time step in seconds (default: 120).

### `gpt2_(self, prompt)`
Generates a response using GPT-2 for a given prompt.

### `last_256_bits(self, input_string)`
Extracts the last 256 bits of a string and encodes them in Base32.

### `generate_key(self, secret_key, given_timestamp)`
Generates a new key based on the secret key and timestamp.

### `generate_totp(self, timestamp=None)`
Generates a TOTP using the generated key.

### `validate(self, given_totp)`
Validates a given TOTP against the current TOTP.

### `now(self)`
Generates the current TOTP.

### `at(self, timestamp)`
Generates a TOTP for a specific timestamp.

---

## Example Workflow

1. **Initialize the Class**:
   ```python
   secret = "MY_SECRET_KEY"
   lm_totp = LM_TOTP(secret)
   ```

2. **Generate a TOTP**:
   ```python
   otp = lm_totp.now()
   print("Generated OTP:", otp)
   ```

3. **Validate a TOTP**:
   ```python
   is_valid = lm_totp.validate(otp)
   print("Validation Result:", is_valid)
   ```

4. **Generate for a Specific Timestamp**:
   ```python
   specific_totp = lm_totp.at(int(time.time()))
   print("Specific TOTP:", specific_totp)
   ```

---

## Diagrams

### Class Workflow
```plaintext
            User Input
                ↓
        Initialize LM_TOTP
                ↓
   Secret + Timestamp → GPT-2
                ↓
       Generate Key (Base32)
                ↓
       Generate TOTP (pyotp)
                ↓
         Validate or Output
```



## Dependencies
- `transformers`
- `torch`
- `pyotp`
- Standard Python libraries (`time`, `base64`, etc.)

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Security Notes
- Ensure the `secret` is kept secure.
- Consider additional measures to optimize the performance and security of GPT-2.

---

