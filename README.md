### API Documentation

#### Reverse Text
**Endpoint:** `/api/reverse`

**Method:** `GET`

**Description:** Reverses the input text.

**Parameters:**
- 

text

 (query parameter): The text to be reversed.

**Response:**
- `200 OK`: Returns a JSON object with the reversed text.

**Example cURL:**
```sh
curl -X GET "http://localhost:8000/api/reverse?text=example"
```

**Response Example:**
```json
{
  "reversed": "elpmaxe"
}
```

#### Disemvowel Text
**Endpoint:** `/api/disemvowel`

**Method:** `GET`

**Description:** Removes all vowels from the input text.

**Parameters:**
- 

text

 (query parameter): The text to be disemvoweled.

**Response:**
- `200 OK`: Returns a JSON object with the disemvoweled text.

**Example cURL:**
```sh
curl -X GET "http://localhost:8000/api/disemvowel?text=example"
```

**Response Example:**
```json
{
  "disemvoweled": "xmpl"
}
```

#### Check Palindrome
**Endpoint:** `/api/palindrome`

**Method:** `GET`

**Description:** Checks if the input text is a palindrome.

**Parameters:**
- 

text

 (query parameter): The text to be checked.

**Response:**
- `200 OK`: Returns a JSON object indicating whether the text is a palindrome.

**Example cURL:**
```sh
curl -X GET "http://localhost:8000/api/palindrome?text=A%20man%20a%20plan%20a%20canal%20Panama"
```

**Response Example:**
```json
{
  "palindrome": true
}
```

### Test Documentation

#### Test Cases for Reverse Text
- **Test:** 

test_reverse_text_empty


  - **Description:** Tests the reverse text endpoint with an empty string.
  - **Expected Result:** Returns `{"reversed": ""}`.

#### Test Cases for Disemvowel Text
- **Test:** 

test_disemvowel_text_empty


  - **Description:** Tests the disemvowel text endpoint with an empty string.
  - **Expected Result:** Returns `{"disemvoweled": ""}`.

#### Test Cases for Palindrome Check
- **Test:** 

test_palindrome_text_empty


  - **Description:** Tests the palindrome check endpoint with an empty string.
  - **Expected Result:** Returns `{"palindrome": true}`.

- **Test:** 

test_palindrome_text_true


  - **Description:** Tests the palindrome check endpoint with a known palindrome.
  - **Expected Result:** Returns `{"palindrome": true}`.

- **Test:** 

test_palindrome_text_false


  - **Description:** Tests the palindrome check endpoint with a non-palindrome.
  - **Expected Result:** Returns `{"palindrome": false}`.