# Write your MySQL query statement below
SELECT
    t.request_at AS Day,
    ROUND(
        SUM(
            CASE
                WHEN t.status = 'cancelled_by_client'
                    OR t.status = 'cancelled_by_driver'
                THEN 1
                ELSE 0
            END
        ) / COUNT(*), 2
    ) AS 'Cancellation Rate'
FROM Trips t
JOIN Users u1
    ON u1.users_id = t.driver_id
JOIN Users u2
    ON u2.users_id = t.client_id
WHERE u1.banned = 'No'
    AND u2.banned = 'No'
    AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;