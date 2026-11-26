# PortSwigger SQLi Study Checklist

Complete labs in this order and record your own notes:
- [ ] SQL injection in WHERE clause, retrieving hidden data (conceptual basics).
- [ ] SQL injection authentication bypass (understand impact in a lab).
- [ ] Determining number of columns.
- [ ] Finding a column with a useful data type.
- [ ] Retrieving data from other tables (lab only; understand risk).
- [ ] Blind SQL injection with conditional responses.
- [ ] Blind SQL injection with conditional errors.
- [ ] Visible error-based behaviour.
- [ ] Time delays and conditional time delays.
- [ ] Out-of-band interaction (advanced; lab only).

For each lab write:
1. What was the vulnerable input?
2. What was the query context?
3. Which technique was used?
4. What response difference proved the issue?
5. What was the minimum proof?
6. What is the correct remediation?

Do not transfer lab data-extraction payloads to a real banking system. On an interview target, follow the given scope and use minimal proof.
