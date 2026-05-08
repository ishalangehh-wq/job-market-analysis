-- View dataset
SELECT * FROM jobs;

-- Top job roles
SELECT job_title, COUNT(*) AS total_jobs
FROM jobs
GROUP BY job_title
ORDER BY total_jobs DESC;

-- Average salary by role
SELECT job_title, AVG(salary) AS avg_salary
FROM jobs
GROUP BY job_title;

-- Top locations
SELECT location, COUNT(*) AS total_jobs
FROM jobs
GROUP BY location
ORDER BY total_jobs DESC;

-- Skills demand
SELECT skills, COUNT(*) AS demand
FROM jobs
GROUP BY skills
ORDER BY demand DESC;
