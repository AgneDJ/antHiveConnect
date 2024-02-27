function ClickCounter(props) {
  const [currentCount, setCurrentCount] = React.useState(props.initialCount);

  function incrementCount() {
    setCurrentCount(currentCount + 1);
  }

  return (
    <div>
      <div>{currentCount}</div>
      <button type="button" onClick={incrementCount}>
        Click me to increase the count
      </button>
    </div>
  );
}

ReactDOM.render(
  <ClickCounter initialCount={0} />,
  document.querySelector("#root")
);
