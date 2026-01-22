async function submitForm() {
  const formData = new FormData();
  formData.append("resume", document.getElementById("resume").files[0]);
  formData.append("job_description", document.getElementById("job").value);

  const response = await fetch("http://127.0.0.1:8000/match", {
    method: "POST",
    body: formData
  });

  const data = await response.json();
  document.getElementById("result").innerText =
    `Match Score: ${data.match_score}%`;
}
