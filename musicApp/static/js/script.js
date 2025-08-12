// side-bar-menu 



const menuOpen = document.getElementById('menu-open');
const menuClose = document.getElementById('menu-close');
const sidebar = document.querySelector('.container .sidebar');

menuOpen.addEventListener('click', () => sidebar.style.left = '0');

menuClose.addEventListener('click', () => sidebar.style.left = '-100%');


// player-bar-menu 

const playerOpen = document.querySelectorAll('.player-open-btn')
const playerClose = document.getElementById('player-close-btn')
const playerbar = document.querySelector('.container .right-section .music-player')
const container = document.querySelector('.container')

playerClose.addEventListener('click', () => {
    playerbar.classList.add('active');
    container.classList.add('active-container');

    if (!song.paused) {
        playPause();
    }
});

playerOpen.forEach(a => {
    a.addEventListener('click', () => {
        playerbar.classList.remove('active');
        container.classList.remove('active-container');
    });
});


// favourite-songs-list


function toggleDropdown() {
  document.getElementById("dropdownItems").classList.toggle("show");
}

function selectItem(name, url) {
  document.getElementById("dropdownButton").innerText = name;
  window.location.href = url; 
}

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}
function toggleFavorite(songId) {
    fetch(`/toggle-fav/${songId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken()
        }
    })
    .then(res => res.json())
    .then(data => {
        const icon = document.querySelector(`#fav-btn-${songId} .bxs-heart`);
        if (data.is_fav) {
            icon.classList.add('active');
        } else {
            icon.classList.remove('active');
        }
    });
}


// create-playlist-overlay-functions

document.addEventListener('DOMContentLoaded', () => {
    const createPlaylistButton = document.querySelectorAll('.create-playlist-button');
    const overlay = document.querySelector('.create-playlist-overlay');
    const closeOverlay = document.querySelector('.close-overlay-button');
    const submitOverlay = document.querySelector('.submit-overlay-button');
    const form = document.querySelector('.create-new-form form');
    const preview = document.getElementById('image-preview');
    const defaultSrc = preview.getAttribute('data-default-src');

    createPlaylistButton.forEach(button => {
        button.addEventListener('click', () => {
            overlay.classList.remove('hidden');
            document.querySelector('.container').style.filter = 'brightness(65%)';
        });
    });

    submitOverlay.addEventListener('click', (e) => {
        
        overlay.classList.add('hidden');
        document.querySelector('.container').style.filter = 'brightness(100%)';

        setTimeout(() => {
            if (form) {
            form.submit();
            form.reset();
            preview.src = defaultSrc;
            preview.style.display = 'block';
            }
            }, 500); 
    });

    closeOverlay.addEventListener('click', () => {
        overlay.classList.add('hidden');
        document.querySelector('.container').style.filter = 'brightness(100%)';

        setTimeout(() => {
            if (form) {
            form.reset();
            preview.src = defaultSrc;
            preview.style.display = 'block';
            } else {
                form.reset();
            }
            }, 500); 
    });

});
    

document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.querySelector('.create-new-form-image');
    const preview = document.getElementById('image-preview');

    fileInput.addEventListener('change', function () {
        const file = this.files[0];
        if (file) {
            const reader = new FileReader();

            reader.onload = function (e) {
                preview.setAttribute('src', e.target.result);
                preview.style.display = 'block';
            };

            reader.readAsDataURL(file);
        }
    });
});

//--------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", function () {
    const sideProgress = document.querySelector('side-progress');
    function level1() {
        sideProgress.classList.add('side-progress-level1');
    }
    function level2() {
        sideProgress.classList.add('side-progress-level2');
    }
    function level3() {
        sideProgress.classList.add('side-progress-level3');
    }
    function level4() {
        sideProgress.classList.add('side-progress-level4');
    }
});
//--------------------------------------------------------------------------




// music-player-controls
// html elementleri js'de nesne gibi davranır.(default özellikler*)

function formatTime(seconds) {
    if (isNaN(seconds)) return "00:00";
    const minutes = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${minutes}:${secs < 10 ? '0' : ''}${secs}`;
}

let progress = document.getElementById("progress-slide");
let song = document.getElementById("active_song");
let controlMusic = document.getElementById("play-button");

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("duration").innerHTML = formatTime(song.duration);
});

song.onloadedmetadata = function () {
    progress.max = song.duration;
};

progress.onchange = function () {
    const newTime = parseFloat(progress.value);
    if (Math.abs(song.currentTime - newTime) > 0.1) {
        song.currentTime = newTime;
    }
};

song.ontimeupdate = function () {
    progress.max = song.duration;
    progress.value = song.currentTime;
    document.getElementById("current-time").innerHTML = formatTime(song.currentTime);
};

function playPause() {
    const currentSongSrc = new URL(source.src).pathname;

    if (song.paused) {
        song.play();
        
        document.querySelectorAll('.run-button').forEach(button => {
            const icon = button.querySelector('.bxs-right-arrow') || button.querySelector('.bx-pause');
            const file = "/media/" + button.dataset.songFile;
            if (file === currentSongSrc) {
                icon.classList.remove('bxs-right-arrow');
                icon.classList.add('bx-pause');
            } else {
                icon.classList.remove('bx-pause');
                icon.classList.add('bxs-right-arrow');
            }
        });

        controlMusic.classList.remove("bxs-right-arrow");
        controlMusic.classList.add("bx-pause");
    } else {
        song.pause();

        document.querySelectorAll('.run-button').forEach(button => {
            const icon = button.querySelector('.bxs-right-arrow') || button.querySelector('.bx-pause');
            const file = "/media/" + button.dataset.songFile;
            if (file === currentSongSrc) {
                icon.classList.remove('bx-pause');
                icon.classList.add('bxs-right-arrow');
            }
        });

        controlMusic.classList.remove("bx-pause");
        controlMusic.classList.add("bxs-right-arrow");
    }
}
song.onplay = function () {
    controlMusic.classList.remove("bxs-right-arrow");
    controlMusic.classList.add("bx-pause");
};

song.onpause = function () {
    controlMusic.classList.remove("bx-pause");
    controlMusic.classList.add("bxs-right-arrow");
};


// Run Music from the list--------------------------------->>


const source = document.getElementById("source");
const img = document.getElementById("image");
const h5_a_name = document.getElementById("a_name");
const h3_m_name = document.getElementById("m_name");
const player_playlist_name = document.getElementById('player-playlist-name');


document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.run-button').forEach(button => {
        button.addEventListener('click', () => {
            const icon = button.querySelector('.bxs-right-arrow') || button.querySelector('.bx-pause');
            if (icon && icon.classList.contains('bx-pause')) {
      
                document.querySelectorAll('.run-button .bx-pause').forEach(icon => {
                icon.classList.remove('bx-pause');
                icon.classList.add('bxs-right-arrow');
                })
                icon.classList.remove('bx-pause');
                song.pause();
            } else {
                const file = button.dataset.songFile;
                const image = button.dataset.songImage;
                const m_name = button.dataset.songMusicName;
                const a_name = button.dataset.songArtistName;
                const p_p_n = player_playlist_name.dataset.playerPlaylistName;

                if (button.classList.contains('not-listed')) {
                    document.querySelectorAll('.run-button .bx-pause').forEach(icon => {
                    icon.classList.remove('bx-pause');
                    icon.classList.add('bxs-right-arrow');
                    });
                
                    if (!file) {
                        console.log(JSON.stringify(button.dataset.songFile))
                        console.error("data-song-file attribute'u yok!");
                        return;
                    }

                    localStorage.setItem("file", file);
                    source.src = "../../media/" + file;

                    localStorage.setItem("image", image);
                    img.src = image;

                    localStorage.setItem("a_name", a_name);
                    h5_a_name.innerHTML = a_name;

                    localStorage.setItem("m_name", m_name);
                    h3_m_name.innerHTML = m_name;

                    player_playlist_name.innerHTML = '_';


                    song.load();

                    song.addEventListener("loadedmetadata", function () {
                        document.getElementById("duration").innerHTML = formatTime(song.duration);
                    });

                    playPause();
                } else {
                    document.querySelectorAll('.run-button .bx-pause').forEach(icon => {
                    icon.classList.remove('bx-pause');
                    icon.classList.add('bxs-right-arrow');
                    });
                
                    if (!file) {
                        console.log(JSON.stringify(button.dataset.songFile))
                        console.error("data-song-file attribute'u yok!");
                        return;
                    }

                    localStorage.setItem("file", file);
                    source.src = "../../media/" + file;

                    localStorage.setItem("image", image);
                    img.src = image;

                    localStorage.setItem("a_name", a_name);
                    h5_a_name.innerHTML = a_name;

                    localStorage.setItem("m_name", m_name);
                    h3_m_name.innerHTML = m_name;

                    player_playlist_name.innerHTML = p_p_n;


                    song.load();

                    song.addEventListener("loadedmetadata", function () {
                        document.getElementById("duration").innerHTML = formatTime(song.duration);
                    });

                    playPause();
                    
                }
            
                

            };
        });
    });
});


