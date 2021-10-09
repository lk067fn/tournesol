This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app), using the [Redux](https://redux.js.org/) and [Redux Toolkit](https://redux-toolkit.js.org/) template.

## Setup

This frontend works using Tournesol's backend from [this repository](https://github.com/tournesol-app/tournesol-backend)

Setup:
1. On the backend repository, start the backend server using the script `dev-env/run-docker-compose.sh` 
2. On the frontend repository, install frontend dependencies: `yarn install`
3. Generate openapi service with the script `generate-services-from-openapi.sh` 
4. Start the local frontend server: `yarn start`

## Available Scripts

In the project directory, you can run:

### `yarn install`

Install all dependencies from `package.json`

### `yarn start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `yarn lint`

Runs the linter and returns lint errors.

This check is automatically enforced on commit using a pre-commit hook. Use `git commit --no-verify` to bypass this check (e.g. to commit on a branch with work in progress).

### `yarn lint:fix`

Attempts to fix lint problems automatically using `eslint --fix`.<br />
This is especially useful to apply `prettier` format rules, if they are not enforced by your IDE.

### `yarn test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `yarn build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `yarn eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).