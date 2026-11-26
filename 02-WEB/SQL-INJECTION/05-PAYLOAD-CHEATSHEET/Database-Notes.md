# Database Syntax Notes

This is a high-level reminder, not a fingerprinting or exploitation guide.

| Database | Common clues / syntax family | Important caution |
|---|---|---|
| MySQL / MariaDB | `#` comments may be accepted; `SLEEP()` exists | Version, SQL mode and query context change behaviour |
| Microsoft SQL Server | `--` comments; `WAITFOR` syntax exists | Permissions and driver behaviour matter |
| PostgreSQL | `--` and `/* */` comments; different function syntax | Do not infer product from one error string |
| Oracle Database | Oracle-specific SQL grammar and functions | Query context and privileges affect tests |
| SQLite | Embedded database; SQL syntax differs in places | Error text may be hidden by the application |

Do not rely on a single error message or banner to identify the database. Report a DB product only when supported by reliable evidence.
