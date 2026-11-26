# Parameter Discovery

## Common locations
- URL query parameters: `?id=10`
- Form fields: `username`, `search`, `category`
- JSON body properties
- Cookies
- Selected HTTP headers
- Sorting, filtering, pagination and report parameters
- Hidden fields and API object properties

## Practical process
1. Browse the whole application with a test account.
2. Capture requests in Burp HTTP history.
3. List parameters and their expected data types.
4. Identify which parameters influence returned records or search results.
5. Test one input at a time.
6. Keep a parameter inventory.

## Parameter inventory
| Request / endpoint | Parameter | Location | Expected type | Function | Tested? |
|---|---|---|---|---|---|
| | | Query / body / JSON / cookie / header | | | |

Do not assume every input reaches a database. Confirm behaviour before drawing a conclusion.
