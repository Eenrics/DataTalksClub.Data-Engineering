Solution

- run through documentation: https://kestra.io/docs/workflow-components/triggers/schedule-trigger

```yml
triggers:
  - id: daily
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "@daily"
    timezone: America/New_York
```

Answer

```md
America/New_York
```
