# review-router demo

A tiny app used to show [review-router](https://github.com/eugeniughelbur/jev-engineering/tree/main/review-router) on real pull requests.

Every pull request runs two routers side by side:

- **A path rule**, the kind most teams start with: full AI review only when a pull request touches CI, auth, migration or dependency files.
- **review-router**, which reads what the diff adds.

Open the pull requests to see where the two routers disagree.
