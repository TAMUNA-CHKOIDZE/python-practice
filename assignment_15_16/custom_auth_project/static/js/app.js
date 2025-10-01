console.log('Confetti check started');
// კონფეტი მხოლოდ მაშინ, თუ URL-ში პარამეტრი `?confetti=1` წერია
const urlParams = new URLSearchParams(window.location.search);
if (urlParams.get('confetti') === '1' && !sessionStorage.getItem('confettiShown')) {
    console.log('Launching confetti');
    confetti({
        particleCount: 300,
        spread: 180,
        origin: {y: 0.6},
        scalar: 1.5,
        ticks: 200,  // ხანგრძლივობა
    });

    sessionStorage.setItem('confettiShown', 'true');
}
