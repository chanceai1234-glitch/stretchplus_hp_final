import sys

css = """
/* ==========================================================================
   Flow Section - Vertical Timeline
   ========================================================================== */
.flow-timeline {
    position: relative;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px 0;
}
.flow-timeline::before {
    content: '';
    position: absolute;
    top: 0;
    left: 40px; /* Line position */
    height: 100%;
    width: 3px;
    background: #e0f2f9; /* light blue line */
}
.timeline-item {
    display: flex;
    margin-bottom: 40px;
    position: relative;
    opacity: 0;
    transform: translateY(20px);
    animation: fadeInUp 0.6s forwards;
}
.timeline-item:nth-child(1) { animation-delay: 0.1s; }
.timeline-item:nth-child(2) { animation-delay: 0.2s; }
.timeline-item:nth-child(3) { animation-delay: 0.3s; }
.timeline-item:nth-child(4) { animation-delay: 0.4s; }
.timeline-item:nth-child(5) { animation-delay: 0.5s; }
.timeline-item:nth-child(6) { animation-delay: 0.6s; }

.timeline-number {
    position: relative;
    width: 80px;
    height: 80px;
    background: #5fb4d4;
    color: white;
    font-size: 1.8rem;
    font-weight: bold;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    z-index: 2;
    border: 5px solid #fff;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.timeline-content {
    background: #fff;
    border-radius: 12px;
    padding: 30px;
    margin-left: 30px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    flex-grow: 1;
}
.timeline-content h3 {
    font-size: 1.3rem;
    color: #2c2c2c;
    margin-bottom: 15px;
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 10px;
}
.timeline-content p {
    font-size: 0.95rem;
    color: #555;
    line-height: 1.7;
    margin-bottom: 15px;
}
.timeline-image {
    width: 100%;
    height: 200px;
    border-radius: 8px;
    overflow: hidden;
    margin-top: 15px;
}
.timeline-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

@media (max-width: 768px) {
    .flow-timeline::before {
        left: 30px;
    }
    .timeline-number {
        width: 60px;
        height: 60px;
        font-size: 1.3rem;
    }
    .timeline-content {
        margin-left: 20px;
        padding: 20px;
    }
}
"""

with open('style.css', 'a') as f:
    f.write(css)

with open('redesign/style.css', 'a') as f:
    f.write(css)

print("Appended CSS.")
