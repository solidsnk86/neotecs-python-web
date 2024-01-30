const shareButtons = document.querySelectorAll("#share-button");
const textShare = document.getElementById("text");

if (navigator.share) {
  shareButtons.forEach(function (shareButton) {
    shareButton.addEventListener("click", async () => {
      try {
        await navigator.share({
          title: windowdocument.title,
          text: textShare.textContent,
          url: window.location.href,
        });
      } catch (error) {
        console.log("Problemas al compartir", error);
      }
    });
  });
}
