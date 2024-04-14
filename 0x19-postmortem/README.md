![debugging](https://github.com/Badr-Annabi/alx-system_engineering-devops/assets/73182348/5d2fc539-b704-48f5-9ac7-d418946e5efa)



# Technical Postmortem: Debugging a 500 Internal Server Error in an Apache Server using Wordpress.

## Issue Summary:

- Duration: The outage occurred from Thursday, April 11, 2024, at 7:30 PM GMT to Thursday, April 11, 2024, at 9:35 PM GMT.
- Impact: GET requests to the Apache web server resulted in 500 Internal Server Errors instead of serving the expected HTML file for a Holberton WordPress site. Approximately 100% of users were affected.
- Root Cause: The issue was caused by a typo error in a configuration file,(/var/www/html/wp-settings.php) specifically .phpp file extension instead of .php.

### Timeline:
Thursday, April 11, 2024, 9:03 PM GMT: Issue detected, GET requests returning 500 Internal Server Errors.

### Investigation:
- Utilized ps aux command to verify running processes, confirming proper functioning of Apache2.
- Inspected /etc/apache2/sites-available to ensure correct web server configuration.
- Initial attempt with strace did not yield useful information.
- Repeated strace process on the www-data process PID, that makes it revealing an -1 ENOENT error when accessing /var/www/html/wp-includes/class-wp-locale.phpp.
- Identified the error in wp-settings.php as a typo error in the file extension.

### Resolution:
- Corrected the typo in the file extension, changing .phpp to .php, restoring the server's ability to serve content.
- Automation and Prevention: Developed a Puppet manifest to automate error-fixing process, replacing all .phpp extensions in wp-settings.php with .php.
Lessons Learned:

### Application Errors:
- Recognized that the outage stemmed from an application error rather than a web server issue.
- Testing: Emphasized the importance of thorough testing pre-deployment to catch errors like typos.
- Status Monitoring: Highlighted the need for uptime-monitoring services like UptimeRobot for instant outage alerts, facilitating quicker resolution.

## Conclusion:
This incident emphasized the significance of rigorous testing, debugging, and proactive error prevention measures. Leveraging tools like strace and automating error fixes with Puppet enhances our ability to swiftly identify and resolve issues, ensuring a more stable and reliable system.
