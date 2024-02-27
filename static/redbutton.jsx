function RedButton(props) {
  return <button type="button">{props.message}</button>;
}

ReactDOM.render(
  <div>
    <RedButton message="Click me" />
    <RedButton message="Or click me" />
  </div>,
  document.querySelector("#root")
);
