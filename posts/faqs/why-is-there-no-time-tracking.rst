.. title: Why is there no Time Tracking?
.. slug: why-is-there-no-time-tracking
.. date: 2015-10-15 18:08:42 UTC+02:00
.. tags: 
.. category:  FAQs
.. order: 70
.. link: 
.. description: 
.. type: text

*Tough question. There is no consensus about time tracking in agile
methodologies. Some people think agile methodologies are not meant to
include time tracking, while some really need time tracking for a
variety of different reasons. Either way, Taiga is was built to
accommodate multiple use cases.*

So why didn’t we have Time Tracking front and center?
=====================================================

Our own philosophy in Taiga de-emphasizes time tracking and favors
focusing on tasks, sprints and team self-organization without concern
for specific time pressures or with measuring the value delivered by a
developer on a given piece of work using time. When looking at our own
list of priorities, we decided to leave time-tracking out of the scope
of the Taiga core feature set.

Here’s an interesting post that speaks to our thoughts on the matter:
`agileadvice`_ by `Mishkin Berteig`_:

    Some Scrum practitioners think it is wasteful to track the time
    spent by developers and designers on individual tasks. They believe
    that Scrum is only concerned with time when it comes to the time
    boxes of the Sprint and Sprint meetings. Scrum also supports
    sustainable development, which implies working sustainable hours.
    When it comes to the completion of tasks, scrum assumes the team is
    committed to delivering value.

    Some scrum practitioners believe that time tracking promotes bad
    habits such as forcing work into billable hours even though it is
    not. Overall, time tracking in a Scrum environment can do harm and
    undermine the entire framework.

But, of course, agile methodologies are meant to be malleable, so even
if we decided to not implement time tracking as a feature in Taiga,
teams are implementing it by using workarounds (like adding hours in the
task or user story title, etc.)

To accomodate these practices we came out with something that could fit
in any team workflow and solve many different different problems: custom
fields

Solution 1: Set Up Custom fields
================================

You can create `custom fields`_ in issues, tasks and user stories to
track everything and make beautiful reports with your favourite
spreadsheet and the `CSV reports`_ functionality.

Solution 2: Using Toggl
=======================

`Toggl`_ is a time tracking app operated by Toggl OÜ that is integrated
with Taiga.io. You only need to sign in in Toggl.com and install the
`Chrome extension`_ to use it over Taiga.io.

Thanks to `Olegerm`_ who developed this integration between Toggl and
Taiga.io

.. _agileadvice: http://www.agileadvice.com/2013/07/29/referenceinformation/the-rules-of-scrum-i-do-not-track-my-hours-or-my-actual-time-on-tasks/
.. _Mishkin Berteig: http://www.agileadvice.com/author/mishkin-berteig/
.. _custom fields: /support/custom-fields
.. _CSV reports: /support/csv-reports
.. _Toggl: https://www.toggl.com/
.. _Chrome extension: https://github.com/toggl/toggl-button
.. _Olegerm: https://github.com/olegermV
